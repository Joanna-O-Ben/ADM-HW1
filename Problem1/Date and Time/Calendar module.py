# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

if __name__ == '__main__':
    s = input()
    s = s.split(" ")

    month = int(s[0])
    day = int(s[1])
    year = int(s[2])

    c = calendar.weekday(year, month, day)
    # print(c)

    if c == 0:
        print("MONDAY")
    elif c == 1:
        print("TUESDAY")
    elif c == 2:
        print("WEDNESDAY")
    elif c == 3:
        print("THURSDAY")
    elif c == 4:
        print("FRIDAY")
    elif c == 5:
        print("SATURDAY")
    elif c == 6:
        print("SUNDAY")