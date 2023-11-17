"""
C - いっしょ
https://atcoder.jp/contests/abc043/tasks/arc059_a
"""

N = int(input())
A = list(map(int, input().split()))
result = []

for y in range(min(A), max(A) + 1):
    cost = 0
    for x in A:
        cost += (x - y) ** 2
    result.append(cost)
    
print(min(result))
