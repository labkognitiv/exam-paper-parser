#!/usr/bin/env python3
"""Serve the reviewer and persist prototype-only review state."""

from __future__ import annotations

import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parent
STATE_FILE = ROOT / "review-state.json"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path == "/api/reviews":
            self.send_json(load_state())
            return
        super().do_GET()

    def do_POST(self):
        if self.path != "/api/reviews":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        try:
            payload = json.loads(self.rfile.read(length))
            question_id = payload["question_id"]
            review = payload["review"]
            if review.get("decision") not in {"pass", "flag"}:
                raise ValueError("invalid decision")
            state = load_state()
            state[question_id] = review
            STATE_FILE.write_text(json.dumps(state, indent=2) + "\n")
            self.send_json({"ok": True})
        except (json.JSONDecodeError, KeyError, ValueError) as exc:
            self.send_json({"ok": False, "error": str(exc)}, status=400)

    def send_json(self, payload, status=200):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def load_state():
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text())
    except json.JSONDecodeError:
        return {}


if __name__ == "__main__":
    print("Internal question reviewer: http://127.0.0.1:8771")
    ThreadingHTTPServer(("127.0.0.1", 8771), Handler).serve_forever()
