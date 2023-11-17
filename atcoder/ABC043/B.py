"""
B - バイナリハックイージー
https://atcoder.jp/contests/abc043/tasks/abc043_b
"""

s = str(input())
result = []

for s_ in list(s):
    if s_ == "0" or s_ == "1":
        result.append(s_)
    elif len(result) > 0:
        result.pop(-1)
print("".join(result))
