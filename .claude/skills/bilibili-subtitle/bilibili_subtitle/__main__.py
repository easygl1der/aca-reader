"""
Bilibili Subtitle CLI entry point.

Usage:
    python -m bilibili_subtitle <url> [options]
    python -m bilibili_subtitle --check
"""

import sys

from .preflight import main as preflight_main


def main() -> int:
    # Check if running preflight only
    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        return preflight_main()

    # TODO: Implement full CLI
    print("Full CLI not implemented yet. Use preflight --check for now.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
