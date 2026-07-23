from sqlalchemy import select

from app.db.models import Product

from app.repositories.base_repository import BaseRepository


class ProductRepository(
    BaseRepository[Product]
):

    model = Product

    async def get_by_odoo_id(
        self,
        odoo_id: int,
    ) -> Product | None:

        stmt = select(Product).where(
            Product.odoo_id == odoo_id
        )

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()