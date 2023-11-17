"""
美しい文字列
https://atcoder.jp/contests/abc044/tasks/abc044_b
"""

w = str(input())
alphabets_count = [0] * 26

for w_ in w:
    alphabets_count[ord(w_) - 97] += 1

for alphabet_count in alphabets_count:
    if alphabet_count % 2 == 1:
        print("No")
        break
print("Yes")
