"""
C020:残り物の量
https://paiza.jp/challenges/73/ready
"""

# 生鮮食品を m[kg] 
# m[kg] のうち p[%] を売ることができた
# 売れ残った量のうち q[%] が売れた
m, p, q = map(int, input().split())

# 売れ残りを定義
m_prime = m - m * p * 0.01

m_prime = m_prime - m_prime * q * 0.01

print(m_prime)
