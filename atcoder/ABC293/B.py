N = int(input())
A = list(map(int, input().split()))

Ns = [(i + 1) for i in range(N)]
called_nums = []

for i in range(N):
    if (i + 1) not in called_nums:
        called_nums.append(A[i])
    called_nums = list(set(called_nums))

X = list(set(Ns) ^ set(called_nums))

print(len(X))
print(*X)
