# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

N = []
for _ in range(T):
    array = list(map(str, input().split()))
    for ar in array:
        N.append(ar)

# print(T)
# print(N)

for i in N:
    # print(i, type(i))
    if not i.isalnum() and "." in i:
        try:
            i = float(i)
            print(True)
        except Exception:
            print(False)
    else:
        print(False)