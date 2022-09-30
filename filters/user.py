import datetime
from typing import Union

from aiogram.dispatcher.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from emoji import demojize
from sqlalchemy import insert, update, select

from database import types
from loader import db


class UserFilter(BaseFilter):
    async def __call__(self, tg_object: Union[Message, CallbackQuery]) -> bool:
        usr = tg_object.from_user
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
        return True
