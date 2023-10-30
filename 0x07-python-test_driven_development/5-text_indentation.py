#!/usr/bin/python3
"""
This module defines `text_indentation`
The function prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines
    Args:
        text: input string
    Returns:
        No return
    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    x = 0
    while a < len(text):
        if flag == 0:
            if text[x] == ' ':
                x += 1
                continue
            else:
                flag = 1
        if flag == 1:
            if text[x] == '?' or text[x] == '.' or text[x] == ':':
                print(text[x])
                print()
                flag = 0
            else:
                if text[x + 1] == '\n':
                     x += 1
                     continue 
                print(text[x], end="")
           x += 1
