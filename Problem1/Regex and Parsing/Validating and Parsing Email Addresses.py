# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re

n = int(input())
for _ in range(n):
    l1, l2 = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', l2)
    if m:
        l2 = l2.replace('<', '').replace('>', '')
        result = email.utils.formataddr((l1, l2))
        print(result)