# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
s = ""

for i in range(N):
    s += input()

s = re.sub(r"(?:<!--(.|\s)*?(?:-->))", "", s)
tags = re.compile(r"(?<=<)(?:.*?)(?=>)").findall(s)

for tag in tags:
    if tag[0] == "/":
        print("End   :", tag[1:])
    else:
        atts = re.compile(r"([\w-]+)(?:=[\"'](.*?)[\"'])?").findall(tag)
        if tag[-1] == "/":
            print("Empty :", atts[0][0])
        else:
            print("Start :", atts[0][0])

        for i in range(1, len(atts)):
            at = atts[i][0]
            if atts[i][1] == '':
                no = 'None'
            else:
                no = atts[i][1]
            print("-> {} > {}".format(at, no))