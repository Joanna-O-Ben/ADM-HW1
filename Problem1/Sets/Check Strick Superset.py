# Enter your code here. Read input from STDIN. Print output to STDOUT

a = set(map(str, input().split(' ')))
is_strict_superset = []
for i in range(int(input())):
    is_strict_superset.append(a.issuperset(set(map(str, input().split(' ')))))
print(all(is_strict_superset))
