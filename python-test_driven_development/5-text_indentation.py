#!/usr/bin/python3
"""Module that defines a text indentation function.

Provides text_indentation which prints text with two newlines after
each '.', '?', and ':' character while trimming line edge spaces.
"""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' and ':' character."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    length = len(text)
    while i < length and text[i] == ' ':
        i += 1
    while i < length:
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1
