from app.dto.get_consultar_geral_dto import GetConsultaGeralSeniorDTO


class CreateConsultaGeralMapper:

    @staticmethod
    def create(dto: GetConsultaGeralSeniorDTO):
        return {
            "codEmp":str(dto.codigo_empresa),
            "codFil":str(dto.codigo_filial),
            "identificadorSistema": "TL",
            "datEmiIni": "20/12/2025",
            "datEmiFim": "31/12/2025",
        }