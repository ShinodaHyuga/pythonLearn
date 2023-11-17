"""
【階段の上り方】階段の上り方 3
https://paiza.jp/works/mondai/dp_primer/dp_primer_stairs_boss/edit?language_uid=python3
"""

# 入力を読み込む
n, a, b, c = map(int, input().split())

# DP配列を用意する
dp = [0] * (n + 1)

# 初期条件を入力する
dp[0] = 1

# 漸化式に従ってDPを実装する
for i in range(1, n + 1):
    # a歩以上いけるとき
    if i >= a:
        dp[i] = dp[i] + dp[i - a]
    # b歩以上いけるとき
    if i >= b:
        dp[i] = dp[i] + dp[i - b]
    # c歩以上いけるとき
    if i >= c:
        dp[i] = dp[i] + dp[i - c]
        
# 出力する
print(dp[-1])
