def f(N: int, H: list) -> int:
    dp = [0, abs(H[0] - H[1])]
    for i in range(2, N):
        dp.append(min(
            dp[i - 1] + abs(H[i - 1] - H[i]),
            dp[i - 2] + abs(H[i - 2] - H[i])
        ))
    return dp[-1]

if __name__ == "__main__":
    N = int(input())
    H = list(map(int, input().split()))
    print(f(N, H))
