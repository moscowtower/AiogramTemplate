import handlers
import database
import chat_member_events

import asyncio
import logging
import loader

from filters.chat_type import ChatTypeFilter
from filters.user import UserFilter

from handlers import routers
from middlewares.locale_middleware import LocaleMiddleware

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")
    dp = loader.dp
    bot = loader.bot
    dp.message.middleware(LocaleMiddleware())
    dp.callback_query.middleware(LocaleMiddleware())
    dp.message.filter(ChatTypeFilter(chat_type='private'))
#    dp.include_router(routers.non_sub_router)


    try:
        #await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
