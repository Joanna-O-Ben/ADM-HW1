import re

N = int(input())

for i in range(N):

    a = input().split()

    if len(a) > 1 and '{' not in a:
        a = re.findall(r'#[a-fA-F0-9]{3,6}', "".join(a))
        for i in a:
            print(i)