"""
STEP: 1 最長部分増加列
https://paiza.jp/works/mondai/dp_primer/dp_primer_lis_step0?language_uid=python3
"""

# 入力を読み込む
n = int(input())
A = [int(input()) for _ in range(n)]

# DP配列を用意する
dp = [0] * (n + 1)

# 初期条件を入力する　
dp[1] = 1

# 漸化式に従ってDPを実装する
for i in range(2, n + 1):
    dp[i] = 1
    for j in range(1, i):
        if A[j - 1] < A[i - 1]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))
