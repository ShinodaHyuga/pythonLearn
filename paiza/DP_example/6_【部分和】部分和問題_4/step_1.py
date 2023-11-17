"""
STEP: 1 部分和問題 1
https://paiza.jp/works/mondai/dp_primer/dp_primer_partial_sums_step0?language_uid=python3
"""

# 入力を読み込む
n, x = map(int, input().split())
A = [int(input()) for _ in range(n)]

# DP配列を用意する
dp = [[0] * (x + 1) for _ in range(n)]

# 0 番目のおもり
dp[0][0] = 1
if A[0] <= x:
    dp[0][A[0]] = 1

# 1 番目以降のおもり 
for i in range(1, n):
    for j in range(x + 1):
        ref = dp[i - 1][j]  # ref = reference(参照)の意味
        # コスト不足のとき
        if A[i] > j:
            dp[i][j] = ref
        else:
            ref_back = dp[i - 1][j - A[i]]
            dp[i][j] = ref or ref_back 
print("yes" if dp[n-1][x] else "no")
