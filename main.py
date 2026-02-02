import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

from app.core.executor import run_consulta


if __name__ == "__main__":
    logging.info("Iniciando processo principal...")
    asyncio.run(run_consulta())
    logging.info("Processo finalizado com sucesso!")