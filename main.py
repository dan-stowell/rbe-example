#!/usr/bin/env python3
import sys
import time


def get_greet(who: str) -> str:
    return f"Hello {who}"


def print_localtime() -> None:
    current_time = time.localtime()
    print(time.asctime(current_time))


def main() -> int:
    who = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(get_greet(who))
    print_localtime()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
