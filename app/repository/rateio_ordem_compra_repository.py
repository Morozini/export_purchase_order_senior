

from app.database.models import RateioOrdemCompraApiSenior


class RateioOrdemCompraRepository:

    async def replace_rateios(self, ordem, rateios: list[dict]):

        await RateioOrdemCompraApiSenior.filter(
            ordem_compra=ordem
        ).delete()

        for rateio in rateios:
            await RateioOrdemCompraApiSenior.create(
                ordem_compra=ordem,
                **rateio
            )
