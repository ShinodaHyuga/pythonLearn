"""
STEP: 5 3項間漸化式 1
https://paiza.jp/works/mondai/dp_primer/dp_primer_recursive_formula_step4?language_uid=python3
"""

# 入力を読み込む
k = int(input())

# DP配列を用意する
dp = [0] * k

# 初期条件を入力する
dp[0], dp[1] = 1, 1

# 漸化式に従ってDPを実装する
for i in range(2, k):
    dp[i] = dp[i - 2] + dp[i - 1]
    
# 出力する
print(dp[-1])
