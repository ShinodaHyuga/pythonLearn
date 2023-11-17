"""
【連続列】最長減少連続部分列
https://paiza.jp/works/mondai/dp_primer/dp_primer_lis_continuous_boss/edit?language_uid=python3
"""

# 入力を読み込む
n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))

A = A[::-1]

# DP配列を用意する
dp = [0] * n

# 初期条件を入力する
dp[0] = 1

# 漸化式に従ってDPを実装する
for i in range(1, n):
    if A[i - 1] <= A[i]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = 1
    
# 出力する
print(max(dp))
