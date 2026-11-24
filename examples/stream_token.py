# Tokens are single-use secrets; never print the response.
# Run: rye run python examples/stream_token.py DEVICE_ID [ALLOWED_ORIGIN]
import sys

from mobilerun_sdk import MobilerunSDK, omit


def stream_token(sdk: MobilerunSDK, device_id: str, allowed_origins: list[str] | None = None) -> None:
    device = sdk.devices.from_id(device_id)
    token = device.create_stream_token(
        ttl_seconds=120, allowed_origins=allowed_origins if allowed_origins is not None else omit
    )
    try:
        if not token.key or not token.key_id or not token.expires_at:
            raise RuntimeError("Invalid token response")
    finally:
        if token.key_id:
            sdk.stream_tokens.delete(token.key_id)


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        raise SystemExit("Pass an existing device ID and optional allowed origin")
    stream_token(MobilerunSDK(), sys.argv[1], [sys.argv[2]] if len(sys.argv) == 3 else None)
