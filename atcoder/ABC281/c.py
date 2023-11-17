N, T = map(int, input().split())
A = list(map(int, input().split()))

T_prime = T % sum(A)

for i in range(N):
    # 最後まで流れる
    if T_prime >= A[i]:
        T_prime -= A[i]
    # 途中で終わる
    else:
        print(i + 1, T_prime)
        break
