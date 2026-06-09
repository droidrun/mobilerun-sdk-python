# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = ["QuestionDeliverAnswerParams", "Answer", "AnswerLabel", "AnswerCustom"]


class QuestionDeliverAnswerParams(TypedDict, total=False):
    answers: Required[Iterable[Iterable[Answer]]]

    question_id: Required[Annotated[str, PropertyInfo(alias="questionId")]]


class AnswerLabel(TypedDict, total=False):
    label: Required[str]


class AnswerCustom(TypedDict, total=False):
    custom: Required[str]


Answer: TypeAlias = Union[AnswerLabel, AnswerCustom]
