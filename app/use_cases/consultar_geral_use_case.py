import asyncio
from tortoise.transactions import in_transaction
from zeep.helpers import serialize_object

from app.mappers.create_consultageral_mappper import CreateConsultaGeralMapper
from app.utils.date_utils import br_date_to_date
from app.utils.gerar_data import gerar_data
from app.dto.get_consultar_geral_dto import GetConsultaGeralSeniorDTO
from app.repository.ordem_compra_repository import OrdemCompraRepository
from app.services.get_consulta_geral_senior import GetConsultaGeralService


class ConsultarGeralUseCase:

    def __init__(self, request: dict):
        self.request = request
        self.service = GetConsultaGeralService()
        self.oc_repo = OrdemCompraRepository()

    async def execute(self):
        dto = GetConsultaGeralSeniorDTO(**self.request)

        total_registros = 0
        loop = asyncio.get_running_loop()

        # 🔥 AQUI está a quebra por semana / janela
        for data_ini, data_fim in gerar_data(
            dto.data_inicio,
            dto.data_fim
        ):
            payload = CreateConsultaGeralMapper.create(
                dto,
                data_ini.strftime("%d/%m/%Y"),
                data_fim.strftime("%d/%m/%Y"),
            )

            response = await loop.run_in_executor(
                None,
                self.service.get_ordem_de_compra,
                payload
            )

            response = serialize_object(response)
            ordens = response.get("ordemCompra", [])

            if not ordens:
                continue

            async with in_transaction():
                for oc in ordens:
                    await self.oc_repo.upsert({
                        "codigo_empresa": oc["codEmp"],
                        "codigo_filial": oc["codFil"],
                        "codigo_fornecedor": oc["codFor"],
                        "numero_ordem_compra": oc["numOcp"],
                        "situacao_ordem_compra": oc["sitOcp"],
                        "data_emissao_oc": br_date_to_date(oc["datEmi"]),
                        "data_fechamento_oc": br_date_to_date(oc.get("datFec")),
                        "data_geracao_oc": br_date_to_date(oc["datGer"]),
                        "obs_oc": oc.get("obsOcp"),
                        "valor_original_oc": oc["vlrOri"],
                    })

            total_registros += len(ordens)

        return {
            "status": "ok",
            "total": total_registros
        }
