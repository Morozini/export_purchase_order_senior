from datetime import date, timedelta
from typing import Iterator, Tuple


def gerar_periodos_mensais(
    ano_inicio: int,
    ano_fim: int
) -> Iterator[Tuple[date, date]]:
    for ano in range(ano_inicio, ano_fim + 1):
        for mes in range(1, 13):
            data_inicio = date(ano, mes, 1)

            if mes == 12:
                data_fim = date(ano, 12, 31)
            else:
                data_fim = date(ano, mes + 1, 1) - timedelta(days=1)

            yield data_inicio, data_fim
