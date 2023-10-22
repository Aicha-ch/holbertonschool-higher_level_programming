#!/usr/bin/python3
""" function that prints a text """


def text_indentation(text):
    """
        new line printing

        Raise:
            TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for string in text:
        new_text += string
        if string in [".", "?", ":"]:
            new_text += "\n\n"

    print(new_text)
