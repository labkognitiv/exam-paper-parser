#!/usr/bin/env python3
"""Local development server for Particle Physics Lesson 1 Reviewer prototype."""

from __future__ import annotations

import argparse
import sys
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PROTOTYPE_DIR = Path(__file__).resolve().parent
REPO_ROOT = PROTOTYPE_DIR.parents[4]


class PrototypeHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Serve from prototype directory by default
        super().__init__(*args, directory=str(PROTOTYPE_DIR), **kwargs)

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve the 9702 Lesson 1 Prototype")
    parser.add_argument("--port", type=int, default=8766, help="Port to run the server on (default: 8766)")
    args = parser.parse_args()

    server = ThreadingHTTPServer(("127.0.0.1", args.port), PrototypeHandler)
    url = f"http://localhost:{args.port}/"
    print("=" * 65)
    print("Physics 9702 · Lesson 1 Reviewer Prototype")
    print(f"URL: {url}")
    print(f"Serving from: {PROTOTYPE_DIR}")
    print("Press Ctrl+C to stop.")
    print("=" * 65)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
