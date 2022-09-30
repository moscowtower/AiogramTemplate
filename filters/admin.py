from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from config import bot_config


class AdminFilter(BaseFilter):
    async def __call__(self, tg_object: Union[Message, CallbackQuery]) -> bool:
        return tg_object.from_user.id in bot_config.admins
