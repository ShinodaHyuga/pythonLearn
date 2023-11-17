# 入力を受け取る
H, W = map(int, input().split())
S = []

[S.append(list(input())) for _ in range(H)]  # 文字列をリストに変換して扱う

for i in range(H):
    for j in range(W - 1):
        # i-1 番目と i 番目が T であるかの判定を行い、そうであったら P と C に変換する
        if S[i][j] == "T" and S[i][j + 1] == "T":
            S[i][j] = "P"
            S[i][j + 1] = "C"

# リストを文字列に変換して出力
[print("".join(S[i])) for i in range(H)]
