memo = {}

def fib(n: int) -> int:
    if n in memo:
        return memo[n]
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)
    memo[n] = result
    return result

if __name__ == "__main__":
    N = 100
    print(fib(N))
