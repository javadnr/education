from sqlalchemy import select

from app.db.models import Contact

from app.repositories.base_repository import BaseRepository


class ContactRepository(
    BaseRepository[Contact]
):

    model = Contact

    async def get_by_odoo_id(
        self,
        odoo_id: int,
    ) -> Contact | None:

        stmt = select(Contact).where(
            Contact.odoo_id == odoo_id
        )

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()
    
    async def upsert(self, odoo_id: int, data: dict) -> Contact:
        existing = self.get_by_odoo_id(odoo_id)
        
        if existing:
            for key, value in data.items():
                setattr(existing, key, value)
            self.session.flush()
            return existing
        
        new_contact = Contact(odoo_id=odoo_id, **data)
        
        return self.add(new_contact)