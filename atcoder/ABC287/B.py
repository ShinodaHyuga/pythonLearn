N, M = map(int, input().split())
S = [str(input()) for _ in range(N)]
T = [str(input()) for _ in range(M)]

result = 0

for s in S:
    for t in T:
        if t in s[-3:]:
            result += 1
            break
        
print(result)
