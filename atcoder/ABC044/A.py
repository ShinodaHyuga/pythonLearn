"""
高橋君とホテルイージー
https://atcoder.jp/contests/abc044/tasks/abc044_a
"""

N = int(input())
K = int(input())
X = int(input())
Y = int(input())

price = 0

for _ in range(min(N, K)):
    price += X
for _ in range(N - K):
    price += Y

print(price)
