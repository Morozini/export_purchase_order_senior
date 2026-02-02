from datetime import date
from pydantic import BaseModel


class GetConsultaGeralSeniorDTO(BaseModel):
    codigo_empresa: int
    codigo_filial: int
    data_inicio: date
    data_fim: date