from aiogram import Router
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER
from aiogram.types import ChatMemberUpdated

from app.bot.logic import is_chinese_gangster

router = Router()


@router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def on_user_join(event: ChatMemberUpdated):

    if await is_chinese_gangster(event):
        await event.bot.ban_chat_member(event.chat.id, event.from_user.id)
        return await event.answer_photo(
            'https://sun1-96.userapi.com/s/v1/ig2/B2wEZxIUPPdxJqmkvdVW7vd8BEh63oD-M9UaeEb6Dwsr6smMiRYpe7FQL4ZwVzG0sLpYc4mM37vDRBduerAc0Ky3.jpg?quality=96&as=32x20,48x30,72x44,108x67,160x99,240x148,360x222,480x296,540x333,640x394,720x444,1080x665,1280x788,1440x887,2560x1577&from=bu&u=mJZuczk_8lr5IO1uVcc5fMN7tt4pJevfp3Pc1QSEdUs&cs=1280x788',
            caption='Ти хто? Твая мая панимать?\n屁股上的老二' # Жёлтолицый гангстер-террорист был забанен
        )
    ...
