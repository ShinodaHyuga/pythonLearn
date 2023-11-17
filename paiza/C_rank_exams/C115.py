"""
C115:渋滞の距離
https://paiza.jp/challenges/560/ready
"""

# 車の数を表すN，渋滞を定義するM，車間を表すA
N, M = map(int, input().split())
A = [int(input()) for _ in range(N - 1)]

# 渋滞の長さを定義
result = 0

for a in A:
    if a <= M:
        result += a
        
print(result)
