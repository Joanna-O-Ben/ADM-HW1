# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
from collections import Counter

shoes_qty = input()
shop_slist = Counter(list(map(int, input().split())))
usrs_qty = input()
earned = 0
if re.match(r'^[1-9][0-9]{0,3}', shoes_qty) and re.match(r'^[1-9][0-9]{0,2}|^1000', usrs_qty):
    for usr in range(0, int(usrs_qty)):
        usr_size, usr_price = map(int, input().split())
        if shop_slist[usr_size] > 0:
            earned += usr_price
            shop_slist[usr_size] -= 1

    print(earned)
