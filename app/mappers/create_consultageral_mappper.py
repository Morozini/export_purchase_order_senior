from app.dto.get_consultar_geral_dto import GetConsultaGeralSeniorDTO


class CreateConsultaGeralMapper:

    @staticmethod
    def create(dto: GetConsultaGeralSeniorDTO):
        return {
            "codEmp":str(dto.codigo_empresa),
            "codFil":str(dto.codigo_filial),
            "codFor": "11121",
            "identificadorSistema": "TL",
            "numOcp": 8469
            # "datEmiIni": "22/12/2025",
            # "datEmiFim": "22/12/2025",
        }