"""
C123:節分ロボット
https://paiza.jp/challenges/600/ready
"""

# 入力を読み込む
N = int(input())
Y = []
for _ in range(N):
    Y.append(int(input()))
    
M = int(input())
A, B, C = [], [], []
for _ in range(M):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

# 出力用の配列を用意する
result = [0 for _ in range(N)]

# 命令の数だけループを回す
for i in range(M):
    # A_i 番目から B_i 番目の参加者に
    for j in range(A[i], B[i] + 1):
        # C_i 個の豆を配る
        result[j - 1] += C[i]

for i in range(N):
    # 自分の年齢を超える豆を受け取ったとき
    if Y[i] < result[i]:
        result[i] = Y[i]
    print(result[i])
