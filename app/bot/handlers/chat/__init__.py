from aiogram import Router

from . import wiki, ping, chat_gpt
from .events import user_join, user_leave

chat_router = Router(name='chat router')
chat_router.include_routers(
    wiki.router,
    ping.router,
    chat_gpt.router,
    user_join.router,
    user_leave.router
)
