# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S = input()
k = input()

p = re.compile(k)
r = p.search(S)

if not r:
    print("(-1, -1)")
while r:
    print("({0}, {1})".format(r.start(), r.end() - 1))
    r = p.search(S, r.start() + 1)