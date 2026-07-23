from typing import Generic, TypeVar

from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

Model = TypeVar("Model")


class BaseRepository(Generic[Model]):

    model = None

    def __init__(
        self,
        session: AsyncSession,
    ):
        self.session = session

    async def get(
        self,
        id_: int,
    ) -> Model | None:

        stmt = select(self.model).where(
            self.model.id == id_
        )

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def add(
        self,
        obj: Model,
    ) -> Model:

        self.session.add(obj)

        await self.session.flush()

        await self.session.refresh(obj)

        return obj

    async def delete(
        self,
        obj: Model,
    ):

        await self.session.delete(obj)

    async def list(self):

        stmt = select(self.model)

        result = await self.session.execute(stmt)

        return result.scalars().all()