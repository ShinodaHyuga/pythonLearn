"""
STEP: 3 最安値を達成するには 3
https://paiza.jp/works/mondai/dp_primer/dp_primer_apples_step2?language_uid=python3
"""

# 入力を読み込む
n, x, a, y, b = map(int, input().split())

dp_num = n + b

# DP配列を用意する
dp = [10001] * dp_num

# 初期条件を入力する　
dp[0] = 0

# 漸化式に従ってDPを実装する
for i in range(2, dp_num):
    dp[i] = min(
        dp[i - x]  + a,
        dp[i - y] + b
    )
    
# 出力する
print(min(dp[n:]))
