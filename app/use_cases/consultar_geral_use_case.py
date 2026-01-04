
from tortoise.transactions import in_transaction
from zeep.helpers import serialize_object
from app.utils.date_utils import br_date_to_date
from app.dto.get_consultar_geral_dto import GetConsultaGeralSeniorDTO
from app.mappers.create_consultageral_mappper import CreateConsultaGeralMapper
from app.repository.ordem_compra_repository import OrdemCompraRepository
from app.repository.rateio_ordem_compra_repository import RateioOrdemCompraRepository
from app.services.get_consulta_geral_senior import GetConsultaGeralService

class ConsultarGeralUseCase:

    def __init__(self, request):
        self.request = request
        self.service = GetConsultaGeralService()
        self.oc_repo = OrdemCompraRepository()
        self.rateio_repo = RateioOrdemCompraRepository()

    async def execute(self):
        dto = GetConsultaGeralSeniorDTO(**self.request)
        payload = CreateConsultaGeralMapper.create(dto)

        response = self.service.get_ordem_de_compra(payload)
        response = serialize_object(response)

        async with in_transaction():
            for oc in response["ordemCompra"]:

                ordem = await self.oc_repo.upsert({
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

                rateios = oc.get("rateio", [])

                await self.rateio_repo.replace_rateios(
                    ordem=ordem,
                    rateios=[
                        {
                            "codigo_empresa": r["codEmp"],
                            "codigo_filial": r["codFil"],
                            "numero_ordem_compra": r["numOcp"],
                            "numero_projeto": r["numPrj"],
                            "codigo_fase": r["codFpj"],
                            "codigo_conta_financeira": r["ctaFin"],
                            "valor_conta_financeira": r["vlrCta"],
                            "codigo_centro_custo": r["codCcu"],
                            "valor_rateado_cc": r["vlrRat"],
                        }
                        for r in rateios
                    ]
                )

        return {
            "status": "ok",
            "total": len(response["ordemCompra"])
        }

