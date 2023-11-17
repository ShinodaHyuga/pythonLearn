"""
C099:折り紙の貼り合わせ
https://paiza.jp/challenges/488/ready
"""

# 入力を読み込む
N, D = map(int, input().split())
D_list = [D] + [int(input()) for _ in range(N - 1)]

# 横幅を定義
widht = D

for i in range(1, N):
    widht += D - D_list[i]
    
# 出力する
print(D * widht)
