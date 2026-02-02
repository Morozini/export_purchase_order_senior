class CreateConsultaGeralMapper:

    @staticmethod
    def create(dto, dat_ini: str, dat_fim: str):
        return {
            "codEmp": str(dto.codigo_empresa),
            "codFil": str(dto.codigo_filial),
            "identificadorSistema": "TL",
            "datEmiIni": dat_ini,
            "datEmiFim": dat_fim,
        }
