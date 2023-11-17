"""
【部分列】最長減少部分列
https://paiza.jp/works/mondai/dp_primer/dp_primer_lis_boss/edit?language_uid=python3
"""

# 入力を読み込む
n = int(input())
A = [int(input()) for _ in range(n)]

# DP配列を用意する
dp = [1] * n

# 漸化式に従ってDPを実装する
for i in range(1, n):
    for j in range(0, i):
        if A[j] > A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 出力する
print(max(dp))
