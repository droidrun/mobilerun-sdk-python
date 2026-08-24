# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConversationAnswerQuestionParams", "Answer", "AnswerLabel", "AnswerCustom", "AnswerUnionMember2"]


class ConversationAnswerQuestionParams(TypedDict, total=False):
    answers: Required[Iterable[Iterable[Answer]]]

    question_id: Required[Annotated[str, PropertyInfo(alias="questionId")]]


class AnswerLabel(TypedDict, total=False):
    label: Required[str]


class AnswerCustom(TypedDict, total=False):
    custom: Required[str]


class AnswerUnionMember2(TypedDict, total=False):
    custom: Required[str]

    label: Required[str]


Answer: TypeAlias = Union[AnswerLabel, AnswerCustom, AnswerUnionMember2]
