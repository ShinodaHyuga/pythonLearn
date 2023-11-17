"""
C097:プレゼント応募企画の実施
https://paiza.jp/challenges/480/show
"""

# これらは応募者が N 人であることを示し、
# X の倍数番目の応募者がプレゼント A の当選者となり、
# Y の倍数番目の応募者がプレゼント B の当選者となることを示します。
N, X, Y = map(int, input().split())

for i in range(N):
    ans = ""
    if (i + 1) % X == 0:
        ans += "A"
    if (i + 1) % Y == 0:
        ans += "B"
    if (i + 1) % X != 0 and (i + 1) % Y != 0:
        ans += "N"
    print(ans)
