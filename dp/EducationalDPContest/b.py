def func(N: int, K: int, H: list) -> int:
    dp = [float("inf") for _ in range(N)]
    dp[0] = 0
    
    for i in range(1, N):
        for j in range(1, min(i + 1, K + 1)):
            dp[i] = min(dp[i], dp[i - j] + abs(H[i - j] - H[i]))
    
    return dp[-1]

if __name__ == "__main__":
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    print(func(N, K, H))
