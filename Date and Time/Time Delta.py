#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    f = '%a %d %b %Y %H:%M:%S %z'
    T1 = datetime.strptime(t1, f)
    T2 = datetime.strptime(t2, f)
    d = (T2 - T1).total_seconds()
    return (abs(int(d)))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)
        # fptr.write(delta + '\n')

    # fptr.close()
