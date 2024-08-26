from aiogram.types import ChatMemberUpdated

from app.utils import contains_chinese_symbols


async def is_chinese_gangster(event: ChatMemberUpdated) -> bool:
    user = event.from_user

    if not contains_chinese_symbols(user.full_name) or user.is_premium:
        return False

    user_profile = await event.bot.get_chat(user.id)
    bio = user_profile.bio
    return bio is None
