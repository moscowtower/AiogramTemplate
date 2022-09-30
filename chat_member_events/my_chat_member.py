from aiogram.types import ChatMemberUpdated

from config import bot_config
from loader import dp, bot
from aiogram.filters.chat_member_updated import (
    ChatMemberUpdatedFilter,
    MEMBER, RESTRICTED,
    KICKED, LEFT,
    ADMINISTRATOR, CREATOR
)


@dp.my_chat_member(ChatMemberUpdatedFilter(
        member_status_changed=
        (KICKED | LEFT | -RESTRICTED)
        >>
        (+RESTRICTED | MEMBER | ADMINISTRATOR | CREATOR)
    ))
async def bot_added(event: ChatMemberUpdated):
    if event.from_user.id not in bot_config.admins:
        await bot.leave_chat(event.chat.id)