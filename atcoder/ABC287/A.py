N = int(input())
S = [str(input()) for _ in range(N)]

if S.count("For") > S.count("Against"):
    print("Yes")
else:
    print("No")
