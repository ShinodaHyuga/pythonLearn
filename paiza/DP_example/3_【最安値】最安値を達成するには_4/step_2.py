"""
STEP: 2 最安値を達成するには 2
https://paiza.jp/works/mondai/dp_primer/dp_primer_apples_step1?language_uid=python3
"""

# 入力を読み込む
n, a, b = map(int, input().split())

dp_num = n + b

# DP配列を用意する
dp = [10001] * dp_num

# 初期条件を入力する

# 漸化式に従ってDPを実装する
for i in range(2, dp_num):
    dp[i] = min(
        dp[i - 2] + a,
        dp[i - 5] + b
    )
print(min(dp[n:]))
