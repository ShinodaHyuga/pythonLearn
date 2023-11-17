"""
STEP: 3 特殊な2項間漸化式 1
https://paiza.jp/works/mondai/dp_primer/dp_primer_recursive_formula_step2?language_uid=python3
"""

# 入力を読み込む
x, d_1, d_2, k = map(int, input().split())

# DP配列を用意する
dp = [0] * k

# 初期条件を入力する
dp[0] = x

# 漸化式に従ってDPを実装する
for n in range(1, k):
    # 第n項が奇数のとき
    if (n + 1) % 2 == 1:
        dp[n] = dp[n - 1] + d_1
    # 第n項が偶数のとき
    else:
        dp[n] = dp[n - 1] + d_2
        
# 出力する
print(dp[-1])

a = int(input())
print(a * 60)
