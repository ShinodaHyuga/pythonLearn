# https://atcoder.jp/contests/abc124/tasks/abc124_a
A, B = map(int, input().split())

max_coin = 0
if A - B > 0:
    print(2 * A - 1)
elif B - A > 0:
    print(2 * B - 1)
else:
    print(2 * A)
