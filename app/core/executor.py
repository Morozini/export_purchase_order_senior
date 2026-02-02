import logging
from datetime import timedelta
from tortoise import Tortoise

from app.use_cases.consultar_geral_use_case import ConsultarGeralUseCase
from app.database.config import init
from app.utils.periodo_utils import gerar_periodos_mensais

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

async def get_empresas_filiais():
    return [
        {"codigo_empresa": 10, "codigo_filial": 1001},
        {"codigo_empresa": 10, "codigo_filial": 1005},
        {"codigo_empresa": 20, "codigo_filial": 2001},
        {"codigo_empresa": 40, "codigo_filial": 4001},
    ]

async def executar_consulta_por_empresa_filial(request: dict):
    logger.info(
        f"Iniciando consulta | Empresa {request['codigo_empresa']} | "
        f"Filial {request['codigo_filial']}"
    )

    use_case = ConsultarGeralUseCase(request)
    result = await use_case.execute()

    logger.info(
        f"Finalizado | Empresa {request['codigo_empresa']} | "
        f"Filial {request['codigo_filial']} | "
        f"Total OC: {result.get('total', 0)}"
    )


async def run_consulta():
    logger.info("Inicializando ORM (Tortoise)...")
    await init()
    logger.info("ORM inicializado com sucesso.")

    try:
        empresas_filiais = await get_empresas_filiais()

        for ef in empresas_filiais:
            for data_inicio, data_fim in gerar_periodos_mensais(2026, 2026):

                logger.info(
                    f"Iniciando | Empresa {ef['codigo_empresa']} | "
                    f"Filial {ef['codigo_filial']} | "
                    f"{data_inicio.strftime('%m/%Y')}"
                )

                request = {
                    "codigo_empresa": ef["codigo_empresa"],
                    "codigo_filial": ef["codigo_filial"],
                    "data_inicio": data_inicio,
                    "data_fim": data_fim,
                }

                use_case = ConsultarGeralUseCase(request)
                result = await use_case.execute()

                logger.info(
                    f"Finalizado | Empresa {ef['codigo_empresa']} | "
                    f"Filial {ef['codigo_filial']} | "
                    f"{data_inicio.strftime('%m/%Y')} | "
                    f"Total OC: {result['total']}"
                )

    finally:
        logger.info("Encerrando conexões com o banco...")
        await Tortoise.close_connections()
        logger.info("Conexões encerradas.")