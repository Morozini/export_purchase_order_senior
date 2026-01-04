import asyncio
from app.core.executor import run_consulta


if __name__ == "__main__":
    asyncio.run(run_consulta())
    print("Processo finalizado com sucesso!")
