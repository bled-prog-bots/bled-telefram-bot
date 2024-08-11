from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode

from app.utils import telegram_markdown_escaping
from app.libs.chatgpt import ChatGptAPI, GPTError, GPTResponse

router = Router(name='chat gpt command router')


@router.message(Command(
    commands=[
        'bled',
        'блед',
        'bled_gpt',
        'gpt',
        'гпт',
        'g',
        'г'
    ],
    prefix='!./',
    ignore_case=True
))
async def chat_gpt_command(msg: Message, chat_gpt: 'ChatGptAPI') -> ...:
    text_split = msg.text.split()

    if len(text_split) == 1:
        return await msg.reply('Неверный синтаксис команды. Не задан вопрос')

    gpt_prompt = ' '.join(text_split[1:])
    loading_placeholder = await msg.reply('🔮')

    gpt_response: GPTError | GPTResponse = await chat_gpt.make_request(gpt_prompt)

    if isinstance(gpt_response, GPTResponse):
        gpt_msg = gpt_response.choices[0].message.content
        gpt_msg_secure = telegram_markdown_escaping(gpt_msg)
        print(gpt_msg_secure)
        return await loading_placeholder.edit_text(
            gpt_msg_secure,
            parse_mode=ParseMode.MARKDOWN
        )

    await loading_placeholder.edit_text(
        f'Ошибка получения ответа от chat gpt: {gpt_response.message}',
        parse_mode=None
    )