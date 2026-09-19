#!/usr/bin/env python3
"""Local JSON persistence for the Physics question reviewer."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


STATE_PATH = Path(__file__).resolve().parent / "review-state.json"
API_PATH = "/api/reviews"
IMAGE_API_PATH = "/api/review-images"
IMAGE_DIR = Path(__file__).resolve().parent / "review-images"
MAX_IMAGE_BYTES = 10 * 1024 * 1024
IMAGE_EXTENSIONS = {"image/png": "png", "image/jpeg": "jpg", "image/webp": "webp"}


def read_state() -> dict:
    try:
        payload = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"reviews": {}}
    reviews = payload.get("reviews", {})
    return {"reviews": reviews if isinstance(reviews, dict) else {}}


def write_review(question_id: str, review: dict) -> dict:
    if not isinstance(question_id, str) or not question_id or not isinstance(review, dict):
        raise ValueError("invalid review entry")
    if review.get("decision") not in {"pass", "flag", "draft"}:
        raise ValueError(f"invalid decision for {question_id}")
    if not isinstance(review.get("note", ""), str) or not isinstance(review.get("updatedAt"), str):
        raise ValueError(f"invalid review for {question_id}")
    attachments = review.get("attachments", [])
    if not isinstance(attachments, list) or any(not isinstance(item, dict) for item in attachments):
        raise ValueError(f"invalid attachments for {question_id}")
    state = read_state()
    state["reviews"][question_id] = review
    temporary = STATE_PATH.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(STATE_PATH)
    return state


class ReviewHandler(BaseHTTPRequestHandler):
    def send_json(self, payload: dict, status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        route = self.path.split("?", 1)[0]
        if route.startswith(f"{IMAGE_API_PATH}/"):
            filename = route.rsplit("/", 1)[-1]
            if not re.fullmatch(r"[A-Za-z0-9_.-]+", filename):
                self.send_error(HTTPStatus.BAD_REQUEST)
                return
            image_path = IMAGE_DIR / filename
            if not image_path.is_file():
                self.send_error(HTTPStatus.NOT_FOUND)
                return
            body = image_path.read_bytes()
            suffix_type = {".png": "image/png", ".jpg": "image/jpeg", ".webp": "image/webp"}
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", suffix_type.get(image_path.suffix, "application/octet-stream"))
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
            return
        if route != API_PATH:
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        self.send_json(read_state())

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path == IMAGE_API_PATH:
            try:
                question_id = parse_qs(parsed.query).get("question_id", [""])[0]
                if not re.fullmatch(r"[A-Za-z0-9_.-]+", question_id):
                    raise ValueError("invalid question id")
                mime_type = self.headers.get("Content-Type", "").split(";", 1)[0]
                extension = IMAGE_EXTENSIONS.get(mime_type)
                if not extension:
                    raise ValueError("paste a PNG, JPEG or WebP image")
                length = int(self.headers.get("Content-Length", "0"))
                if length < 1 or length > MAX_IMAGE_BYTES:
                    raise ValueError("image must be between 1 byte and 10 MB")
                body = self.rfile.read(length)
                digest = hashlib.sha256(body).hexdigest()[:12]
                filename = f"{question_id}-{digest}.{extension}"
                IMAGE_DIR.mkdir(parents=True, exist_ok=True)
                image_path = IMAGE_DIR / filename
                image_path.write_bytes(body)
                attachment = {
                    "name": filename,
                    "path": f"review-images/{filename}",
                    "url": f"{IMAGE_API_PATH}/{filename}",
                    "mimeType": mime_type,
                    "createdAt": self.date_time_string(),
                }
            except (ValueError, OSError) as exc:
                self.send_json({"ok": False, "error": str(exc)}, HTTPStatus.BAD_REQUEST)
                return
            self.send_json({"ok": True, "attachment": attachment}, HTTPStatus.CREATED)
            return
        if parsed.path != API_PATH:
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            if not isinstance(payload, dict):
                raise ValueError("review update must be an object")
            state = write_review(payload.get("question_id", ""), payload.get("review"))
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError, OSError) as exc:
            self.send_json({"ok": False, "error": str(exc)}, HTTPStatus.BAD_REQUEST)
            return
        self.send_json({"ok": True, **state})

    def log_message(self, format: str, *args: object) -> None:
        return


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=3003)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), ReviewHandler)
    print(f"Review state: {STATE_PATH}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
