"""
D - アンバランス
https://atcoder.jp/contests/abc043/tasks/arc059_b
"""

s = str(input())
result = [0] * 26
alpabets = [chr(c) for c in range(97, 123)]

# 文字列の長さが2未満
if len(s) < 2:
    ans = "-1 -1"

else:
    for s_ in s:
        result[ord(s_) - 97] += 1
    # 複数の文字の数が最大値をとる
    if result.count(max(result)) > 1:
        ans = "-1 -1"
    else:
        max_alphabet = chr(result.index(max(result)) + 97)
        
        ans = "{} {}".format(
            s.index(max_alphabet) + 1,
            len(s) - s[::-1].index(max_alphabet)
        )
    
print(ans)
