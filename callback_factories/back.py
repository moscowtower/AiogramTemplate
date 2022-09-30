from typing import Optional
from aiogram.dispatcher.filters.callback_data import CallbackData


class BackFactory(CallbackData, prefix="back"):
    menu: str
    action: Optional[str]
    page: Optional[int]