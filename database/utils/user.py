import datetime
from typing import Union

from emoji.core import demojize
from sqlalchemy import select, update, insert, delete
from database.client import Client
from database import types


async def get_user(db: Client, usr):
    async with db.AsyncSession.begin() as session:
        user = await session.scalar(
            select(
                types.User
            ).filter_by(
                id=usr.id,
                is_banned=False
            )
        )
        if not user:
            await session.execute(
                insert(
                    types.User
                ).values(
                    id=usr.id,
                    first_name=demojize(usr.first_name),
                    username=usr.username
                )
            )
        else:
            await session.execute(
                update(
                    types.User
                ).values(
                    last_active=datetime.datetime.now()
                ).filter_by(
                    id=usr.id
                )
            )
        return user