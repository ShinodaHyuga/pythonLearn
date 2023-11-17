"""
STEP: 4 特殊な2項間漸化式 2
https://paiza.jp/works/mondai/dp_primer/dp_primer_recursive_formula_step3?language_uid=python3
"""

# 入力を読み込む
x, d_1, d_2 = map(int, input().split())
Q = int(input())
K = []

for _ in range(Q):
    K.append(int(input()))
    
# DP配列を用意する
dp = [0] * max(K)

# 初期条件を入力する
dp[0] = x

# 漸化式に従ってDPを実装する
for n in range(1, max(K)):
    # 第n項が奇数のとき
    if (n + 1) % 2 == 1:
        dp[n] = dp[n - 1] + d_1
    # 第n項が偶数のとき
    else:
        dp[n] = dp[n - 1] + d_2
        
# 出力する
for k in K:
    print(dp[k - 1])
