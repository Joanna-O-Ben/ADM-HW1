# Enter your code here. Read input from STDIN. Print output to STDOUT

print(len((set(input().split()) if input() != '-1' else '')|(set(input().split()) if input() != '-1' else '')))
