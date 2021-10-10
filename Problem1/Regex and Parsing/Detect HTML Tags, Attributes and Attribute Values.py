# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])


N = int(input())
l = ""

for i in range(N):
    l += input()

out_put = MyHTMLParser()
out_put.feed(l)