from abc import ABC, abstractstaticmethod

from ..types import AttributeName, TokenAttribute


class TokenStandard(ABC):
    @abstractstaticmethod
    def count_token_attributes(
        self, tokens: list[TokenAttribute], **extras
    ) -> dict[AttributeName, int]:
        raise NotImplementedError()
