# 入力を受け取る
N, D = map(int, input().split())
T = list(map(int, input().split()))

for i in range(1, N):
    # ダブルクリックが成立
    if T[i] - T[i - 1] <= D:
        print(T[i])
        exit()  # 強制終了
print(-1)
