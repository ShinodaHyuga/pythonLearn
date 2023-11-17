"""
STEP: 1 2項間漸化式 1
https://paiza.jp/works/mondai/dp_primer/dp_primer_recursive_formula_step0?language_uid=python3
"""

# 入力を読み込む
x, d, k = map(int, input().split())

# DP配列を用意する
dp = [0] * k

# 初期条件を入力する
dp[0] = x

# 漸化式に従ってDPを実装する
for i in range(1, k):
    dp[i] = dp[i - 1] + d
    
# 出力する
print(dp[-1])
