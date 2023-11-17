# https://atcoder.jp/contests/dp/tasks/dp_d
"""
N, W = map(int, input().split())  # 荷物の個数N、容量W

ws, vs = [], []
for _ in range(N):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)
"""

N = 10
W = 1700

ws = [220, 360, 350, 280, 380, 240, 250, 320, 340, 260]
vs = [418, 360, 455, 616, 608, 360, 425, 640, 374, 546]

N = 12
W = 24

ws = [9, 3, 4, 7, 2, 6, 2, 1, 1, 10, 5, 10]
vs = [4, 2, 2, 10, 7, 1, 2, 9, 3, 2, 8, 9]
dp = [[0] * (W + 1) for i in range(N + 1)]
for i in range(N):
    for w_sum in range(W + 1):
        if w_sum - ws[i] >= 0:
            dp[i+1][w_sum] = max(dp[i][w_sum], dp[i][w_sum - ws[i]] + vs[i])
        else:
            dp[i+1][w_sum] = dp[i][w_sum]

print(dp[N][W])
