N = int(input())
Ss = list(map(int, input().split()))

print(Ss[0], end=" ")
for i in range(1, len(Ss)):
    if i != (len(Ss) - 1):
        print(Ss[i] - Ss[i - 1], end=" ")
    else:
        print(Ss[i] - Ss[i - 1])
