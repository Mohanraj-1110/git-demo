#!/usr/bin/env python3

"""Simple Python demo program."""


def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}! Welcome to the simple Python demo."


def main() -> None:
    name = input("Enter your name: ")
    message = greet(name.strip() or "friend")
    print(message)


if __name__ == "__main__":
    main()
