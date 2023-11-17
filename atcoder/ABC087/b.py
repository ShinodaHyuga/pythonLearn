A = int(input())  # 500円が A 枚
B = int(input())  # 100円が B 枚
C = int(input())  # 50円が C 枚
X = int(input())  # 合計金額

count_cases = sum([
    500 * i + 100 * j + 50 * k == X
    for i in range(A + 1)
    for j in range(B + 1)
    for k in range(C + 1)
])

print(count_cases)
