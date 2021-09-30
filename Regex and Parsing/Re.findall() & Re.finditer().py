# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S = input()
v = 'aeiou'
c = 'qwrtypsdfghjklzxcvbnm'

result = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), S.strip(), flags=re.I)
print('\n'.join(result or ['-1']))