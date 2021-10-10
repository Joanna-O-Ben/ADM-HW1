cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    prev = 1
    curr = 0
    fib = [curr]
    for i in range(n):
        p = curr
        curr = curr + prev
        prev = p
        fib.append(curr)
    return fib[0:n]

    # [0,1,0], [1,1, 1], [1, 2, 1], [2, 3, 2], [3, 5, 3], [5, 8, 5]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))