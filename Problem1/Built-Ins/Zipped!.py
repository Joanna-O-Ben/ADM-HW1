# Enter your code here. Read input from STDIN. Print output to STDOUT


N, X = map(int, input().split())
ar = []
for _ in range(X):
    array = list(map(float, input().split()))
    ar.append(array)

# print(N, X)
# print(ar)

a = zip(*ar)
ele = list(a)
# print(ele)

for i in ele:
    print(sum(i) / X)