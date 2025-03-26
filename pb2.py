def fib(pre, next):
    cur = pre + next
    if cur > 4000000:
        return 0
    else:
        if cur% 2 == 0:
            print(cur)
            return cur+ fib(next, cur)
        else:
            return fib(next, cur)


print("final: ", 2+fib(1, 2))