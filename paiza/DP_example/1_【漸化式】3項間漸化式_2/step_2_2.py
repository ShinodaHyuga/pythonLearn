"""
STEP: 2 2項間漸化式 2
https://paiza.jp/works/mondai/dp_primer/dp_primer_recursive_formula_step1?language_uid=python3
"""

# 入力を読み込む
x, d = map(int, input().split())
Q = int(input())
    
# DP配列を用意する
dp = [0] * (1000 + 1)

# 漸化式に従ってDPを実装する
for i in range(1, 1000 + 1):
    dp[i] = dp[i - 1] + d

# 出力する
for _ in range(Q):
    k = int(input())
    print(dp[k - 1])

n = int(input())
print(n * 60)
