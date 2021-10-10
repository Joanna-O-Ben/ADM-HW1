import re

regex_integer_in_range = r"_________"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"_________"	# Do not delete 'r'.


print(bool(re.match(
    r'^'
    r'(?!.*(.).\1.*(.).\2)'
    r'(?!.*(.)(.)\3\4)'
    r'[1-9]\d{5}'
    r'$', input()
)))

P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)