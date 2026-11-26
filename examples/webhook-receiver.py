# No API key is needed. Set WEBHOOK_SECRET to your endpoint signing secret.
# Usage: python examples/webhook-receiver.py
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

from mobilerun_sdk import WebhookVerificationError, verify_webhook


class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        body = self.rfile.read(int(self.headers.get("Content-Length", "0")))
        try:
            verify_webhook(
                body, {name: self.headers.get_all(name) for name in self.headers}, os.environ["WEBHOOK_SECRET"]
            )
        except WebhookVerificationError:
            self.send_response(400)
        else:
            self.send_response(204)
        self.end_headers()


HTTPServer(("127.0.0.1", int(os.environ.get("PORT", "8080"))), WebhookHandler).serve_forever()
