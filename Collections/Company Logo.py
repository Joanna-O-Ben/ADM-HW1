#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    letters = [0] * 26

    for letter in s:
        letters[ord(letter) - ord('a')] += 1

    for _ in range(3):

        max_letter = max(letters)

        for index in range(26):
            if max_letter == letters[index]:
                print (chr(ord('a') + index), max_letter)
                letters[index] = -1
                break
