from aiogram import Router

from app.bot.filters import IsBledChatFilter
from . import wiki, ping, chat_gpt
from .events import user_join, user_leave


chat_router = Router(name='chat router')

# Фильтр что событие пришло из нашего чата
chat_router.message.filter(
    IsBledChatFilter()
)

chat_router.include_routers(
    wiki.router,
    ping.router,
    chat_gpt.router,
    user_join.router,
    user_leave.router
)
