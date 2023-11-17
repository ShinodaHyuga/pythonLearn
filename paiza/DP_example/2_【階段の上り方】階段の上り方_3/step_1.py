"""
STEP: 1 階段の上り方 1
https://paiza.jp/works/mondai/dp_primer/dp_primer_stairs_step0?language_uid=python3
"""

# 部分問題として、「1 ~ n-1 段の階段を上る方法が何通りあるか」、という問題を考える

# 入力を読み込む
n = int(input())

# DP配列を用意する
dp = [0] * (n + 1)

# 初期条件を入力する
dp[0] = 1  # 0段の階段を上る方法は1通り

# 漸化式に従ってDPを実装する
for i in range(1, n + 1):
    dp[i] = dp[i - 1]
    # 2歩以上進めるとき
    if i > 1:
        dp[i] = dp[i] + dp[i - 2]

# 出力する        
print(dp[-1])
