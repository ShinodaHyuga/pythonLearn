"""
STEP: 1 最安値を達成するには 1
https://paiza.jp/works/mondai/dp_primer/dp_primer_apples_step0?language_uid=python3
"""

# 入力を読み込む
n, a, b = map(int, input().split())

# DP配列を用意する
dp = [0] * (n + 2)  # 0 個から n+1 個の要素を持つ

# 初期条件を入力する
dp[0] = 0
dp[1] = a

# 漸化式に従ってDPを実装する
for i in range(2, n + 2):
    dp[i] = min(
        dp[i - 1] + a,
        dp[i - 2] + b
    )
    
# 出力する
print(min(dp[-2:-1]))
