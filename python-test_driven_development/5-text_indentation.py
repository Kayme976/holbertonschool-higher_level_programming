#!/usr/bin/python3
"""Square class"""


def text_indentation(text):
    """Function that prints a text with 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line_flag = False
    for idx, char in enumerate(text):
        if idx > 0:
            previous_char = text[idx - 1]
            if previous_char in [".", "?", ":"]:
                print("\n")
                new_line_flag = True
                if char == ' ':
                    continue
        if new_line_flag and char == ' ':
            continue
        print(char, end="")
        new_line_flag = False
