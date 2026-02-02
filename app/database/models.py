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
    obs_oc = fields.CharField(max_length=400, null=True, description="obsOcp")
    valor_original_oc = fields.FloatField(description="vlrOri")

    class Meta:
        table = "task_ordem_compra_api_senior"