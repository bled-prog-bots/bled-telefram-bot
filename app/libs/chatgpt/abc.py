from abc import ABC, abstractmethod

from .types import ChatCompletionMessage


class ABCOpenAIAPI(ABC):

    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def get_completion(self, prompt: str) -> ChatCompletionMessage:
        ...
