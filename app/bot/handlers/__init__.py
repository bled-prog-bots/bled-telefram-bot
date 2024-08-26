from aiogram import Router

from . import chat

root_router = Router(name='root router')

root_router.include_routers(
    chat.chat_router
)
