# https://atcoder.jp/contests/abc273/tasks/abc273_b

X, K = map(int, input().split())

# 下一桁から下K桁まで四捨五入を繰り返す
for i in range(1, K + 1):
    # 肩の数値がXの桁数を超えた時
    if X / (10 ** (i - 1)) < 1:
        break
    else:
        # Xの値を一桁ずつ文字列でリストxsに格納
        xs = [x for x in str(X)]
        # round()関数は5を切り捨ててしまうため、次の処理を入れる
        if xs[-i] == "5":
            xs[-i] = "6"
        # 下i桁を四捨五入
        X = round(int("".join(xs)), -i)
print(X)

"""
# 上記のコードをDecimalライブラリを使って書く
from decimal import Decimal, ROUND_HALF_UP
for i in range(1, K + 1):
    X = int(Decimal(X).quantize(Decimal("1e" + str(i)), rounding=ROUND_HALF_UP))
print(X)
"""
