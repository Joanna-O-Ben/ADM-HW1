# Enter your code here. Read input from STDIN. Print output to STDOUT

S = list(input())
# print(S, type(S))

LETTERS = []
low = []
up = []
DIGITS = []
odd = []
even = []

for c in S:
    if c.isalpha():
        LETTERS.append(c)
    if c.isnumeric():
        DIGITS.append(c)
# print(LETTERS, DIGITS)

for s in LETTERS:
    if s.isupper():
        up.append(s)
    else:
        low.append(s)
# print(low, up)

for n in DIGITS:
    n = int(n)
    if n % 2 == 1:
        n = str(n)
        odd.append(n)
    else:
        n = str(n)
        even.append(n)
# print(odd, even)

A = "".join(sorted(low) + sorted(up) + sorted(odd) + sorted(even))
print(A)
