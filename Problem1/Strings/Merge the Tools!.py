from textwrap import wrap

def merge_the_tools(string, k):
    # your code goes here
    w = wrap(string, k)
    # print(w)

    for el in w:
        # print(el)
        l = []
        for let in el:
            # print(let)
            if let not in l:
                l.append(let)
            else:
                continue
        l = "".join(l)
        print(l)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)