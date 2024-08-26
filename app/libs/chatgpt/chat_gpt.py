from openai import OpenAI
from openai.types.chat.chat_completion import Choice
from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam

from .abc import ABCOpenAIAPI
from .types import ChatCompletionsArgs, ChatCompletionMessage


class OpenAIAPI(ABCOpenAIAPI):

    __client: OpenAI
    __completions_settings: ChatCompletionsArgs

    def __init__(self, *, api_key: str, base_url: str, completions_settings: ChatCompletionsArgs) -> None:
        self.__client = OpenAI(
            base_url=base_url,
            api_key=api_key,
        )

        if not isinstance(completions_settings, ChatCompletionsArgs):
            raise # TODO make something

        self.__completions_settings = completions_settings

    async def get_completion(self, prompt: str) -> ChatCompletionMessage:
        model = self.__completions_settings.model
        context = self.__completions_settings.context

        completion = self.__client.chat.completions.create(
            messages=[
                ChatCompletionSystemMessageParam(
                    role='system',
                    content=context
                ),
                ChatCompletionUserMessageParam(
                    role='user',
                    content=prompt
                )
            ],
            model=model
        )

        first_completion: Choice =  completion.choices[0]
        return first_completion.message
