# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())

for lines in range(N):
    l = input()
    if re.match(r'[789]\d{9}$',l) and len(l) == 10:
        print ('YES')
    else:
        print ('NO')