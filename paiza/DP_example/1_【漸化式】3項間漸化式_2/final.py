"""
【漸化式】 3項間漸化式 2
https://paiza.jp/works/mondai/dp_primer/dp_primer_recursive_formula_boss/edit?language_uid=python3
"""

# 入力を読み込む
Q = int(input())
K = []

for _ in range(Q):
    K.append(int(input()))
    
# DP配列を用意する
dp = [0] * max(K)

# 初期条件を入力する
dp[0], dp[1] = 1, 1

# 漸化式に従ってDPを実装する
for i in range(2, max(K)):
    dp[i] = dp[i - 2] + dp[i - 1]
    
# 出力する
for k in K:
    print(dp[k - 1])
