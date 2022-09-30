from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from sqlalchemy import select

from database.types import User
from loader import db


class LocaleMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Union[Message, CallbackQuery], Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        async with db.AsyncSession.begin() as session:
            user_locale = await session.scalar(
                select(
                    User.locale
                ).filter_by(
                    id=event.from_user.id
                )
            )
            data['locale'] = user_locale if (
                user_locale
            ) else event.from_user.language_code.replace('en', 'en_US').replace('de', 'de_DE')
            return await handler(event, data)