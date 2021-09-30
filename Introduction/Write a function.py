def is_leap(year):
    # Write your logic here
    for s in range(1900, 10 ** 5 + 1, 100):
        if year == s and s % 400 != 0:
            return False
    for i in range(1900, 10 ** 5 + 1, 4):
        if year == i:
            return True

    return False


year = int(input())
print(is_leap(year))