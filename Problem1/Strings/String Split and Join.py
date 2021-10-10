def split_and_join(line):
    # write your code here
    for word in line:
        line1 = line.split(" ")
        line2 = "-".join(line1)
        return(line2)

#another way to do it
def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    l = ""
    for lett in line:
        l += lett
    return (l)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)