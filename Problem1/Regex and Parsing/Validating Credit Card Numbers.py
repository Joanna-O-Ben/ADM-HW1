# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())

for i in range(N):
    t = input()
    dash = re.sub("-", "", t)
    cond_1 = re.search("^[456]\d{3}(-?\d{4}){3}$", t)
    cond_2 = re.search(r"(\d)\1{3}", dash)
    if not cond_1 or cond_2:
        print("Invalid")
    else:
        print("Valid")