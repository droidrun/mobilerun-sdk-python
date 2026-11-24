# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExecutionRetrieveParams"]


class ExecutionRetrieveParams(TypedDict, total=False):
    include: Literal["input"]
    """Extra data to add to each step of `result.steps` (loop children included).

    `input` adds a field `input` per step: what the step ran with, resolved after
    templating and without values the platform adds (ids, session and idempotency
    keys, script state). For sandbox steps, nested `input` is the effective input
    when available, otherwise the submitted input. The value is the input object, a
    marker `{ "notRecorded": "too_large" | "invalid" | "unavailable" }` (`too_large`
    adds `bytes`) when it could not be stored or exceeds 64 KiB, or null for a step
    without a recorded input, such as a run from before inputs were stored. Secrets
    are redacted before storing, best effort and by key name only: a value is
    replaced with `[REDACTED]` at any depth when its key, read as words
    (`clientSecret`, `x-auth-token`), contains `password`, `passwd`, `passphrase`,
    `secret`, `token`, `authorization`, `cookie`, `credential`, `signature`,
    `api key`, `private key`, `client key` or `card number`, or is exactly `pwd`,
    `otp`, `totp`, `pin`, `cvv` or `cvc`. `Bearer`, `Basic` and `Token`
    authorization values in strings are masked too. Secrets inside other strings
    (for example agent prompts) or under other key names are not detected. The
    content of file uploads is never stored, only its size, encoding and type.
    Without `include` the response has no `input` fields.
    """
