n = int(input())
s = []
for _ in range(n):
    s.append(input())

cnt = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        cnt[int(s[i][j])] = cnt[int(s[i][j])] + 1

mx = [0 for _ in range(10)]
for i in range(10):
    for j in range(10):
        mx[i] = max(mx[i], 10 * (cnt[i][j] - 1) + j)

print(min(mx))
