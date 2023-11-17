"""
C117:大量出店
https://paiza.jp/challenges/571/ready
"""


# 出店する店舗の数を表す整数 N 
# および営業する月数を表す整数 M 
N, M = map(int, input().split())

# 1 店舗あたりの店舗の建設費用を表す整数 A、
# 1 店舗あたりの毎月の人件費を表す整数 B、
# ラーメン 1 杯あたりの利益を表す整数 C 
A, B, C = map(int, input().split())

# i 番目の店舗が M ヶ月間に販売したラーメンの杯数を表す整数 R_i 
R = [int(input()) for _ in range(N)]

# i 番目の店舗の売上 sales
# 初期値には建設費用を設定
sales = [-1 * A for _ in range(N)]

# 月ごとに人件費と利益を計算
for n in range(N):
    sales[n] += (-1 * B * M) + (C * R[n])
    
# 利益が赤字となっている店舗の数を出力する
print(sum(s < 0 for s in sales))
