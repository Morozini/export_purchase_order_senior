from tortoise import fields
from tortoise.models import Model


class OrdemCompraApiSenior(Model):
    id = fields.IntField(pk=True)

    codigo_empresa = fields.IntField(description="codEmp")
    codigo_filial = fields.IntField(description="codFil")
    codigo_fornecedor = fields.IntField(description="codFor")
    numero_ordem_compra = fields.IntField(description="numOcp")
    situacao_ordem_compra = fields.IntField(description="sitOcp")
    data_emissao_oc = fields.DateField(description="datEmi")
    data_fechamento_oc = fields.DateField(null=True, description="datFec")
    data_geracao_oc = fields.DateField(description="datGer")
    obs_oc = fields.CharField(max_length=255, null=True, description="obsOcp")
    valor_original_oc = fields.FloatField(description="vlrOri")

    class Meta:
        table = "task_ordem_compra_api_senior"
        unique_together = (
            ("codigo_empresa", "codigo_filial", "numero_ordem_compra"),
        )

class RateioOrdemCompraApiSenior(Model):
    id = fields.IntField(pk=True)
    ordem_compra = fields.ForeignKeyField(
        "models.OrdemCompraApiSenior",
        related_name="rateios",
        on_delete=fields.CASCADE
    )
    numero_ordem_compra = fields.IntField(description="numOcp")
    codigo_empresa = fields.IntField(description="codEmp")
    codigo_filial = fields.IntField(description="codFil")
    numero_projeto = fields.IntField(description="numPrj")
    codigo_fase = fields.IntField(description="codFpj")
    codigo_conta_financeira = fields.IntField(description="ctaFin")
    valor_conta_financeira = fields.FloatField(description="vlrCta")
    codigo_centro_custo = fields.IntField(description="codCcu")
    valor_rateado_cc = fields.FloatField(description="vlrRat")

    class Meta:
        table = "task_rateio_ordem_compra_api_senior"