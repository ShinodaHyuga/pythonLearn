# https://atcoder.jp/contests/abc270/tasks/abc270_b

# (X, Y, Z) = (ゴール, 壁, ハンマー)
X, Y, Z = map(int, input().split())

# 壁の座標が原点よりも小さいとき
if Y < 0:
    X, Y, Z = -X, -Y, -Z

# ゴールまでに壁がないとき
if X < Y:
    ans = abs(X)
# 壁を壊す必要があり、ハンマーを取れないとき
elif Y < X and Y < Z:
    ans = -1
# ハンマーを取ってからゴールへ向かうとき
else:
    ans = 2 * abs(Z) + abs(X)

print(ans)
