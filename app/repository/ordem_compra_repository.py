
from app.database.models import OrdemCompraApiSenior


class OrdemCompraRepository:

    async def upsert(self, data: dict) -> OrdemCompraApiSenior:
        obj, _ = await OrdemCompraApiSenior.update_or_create(
            numero_ordem_compra=data["numero_ordem_compra"],
            defaults=data
        )
        return obj