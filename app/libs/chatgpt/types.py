from typing import Union, Optional

from pydantic import BaseModel
from openai.types import chat
from openai.types import ChatModel

__all__ = [
    'ChatCompletionMessage',
    'ChatCompletionsArgs',
]

ChatCompletionMessage = chat.ChatCompletionMessage


class ChatCompletionsArgs(BaseModel):
    model: Union[str, ChatModel]
    context: Optional[str] = None
