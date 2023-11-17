# 入力を受け取る
S = str(input())

# それぞれの文字が何番目にあるかを取得
B_1 = S.find("B") + 1
B_2 = len(S) - S[::-1].find("B")
K_1 = S.find("K") + 1
R_1 = S.find("R") + 1
R_2 = len(S) - S[::-1].find("R")

# 条件の判定
result = "Yes" if (B_1 + B_2) % 2 == 1 and R_1 < K_1 < R_2 else "No"

# 出力
print(result)
