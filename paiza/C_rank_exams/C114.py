"""
C114:しりとりの判定
https://paiza.jp/challenges/555/ready
"""

# 単語の数 N
N = int(input())
S = [str(input()) for _ in range(N)]

for i in range(1, len(S)):
    # i-1 番目の最後の文字と i 番目の最初の文字を比較する
    if S[i - 1][-1] != S[i][0]:
        ans = "{} {}".format(S[i - 1][-1], S[i][0])
        break
    ans = "Yes"
    
# 出力する
print(ans)
