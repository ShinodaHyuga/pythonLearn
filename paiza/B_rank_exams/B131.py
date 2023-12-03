def main(A, RS):
    ans = 0
    for i, rs in enumerate(RS):
        if i == 0:
            prev_r = rs[0]
            prev_s = rs[1]
            ans += A[prev_r][prev_s]
        else:
            curt_r = rs[0]
            curt_s = rs[1]
            ans += abs(A[curt_r][curt_s] - A[curt_r][prev_s])
            prev_r = curt_r
            prev_s = curt_s
    return ans

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    X = int(input())
    RS =[]
    for _ in range(X):
        tmp = list(map(int, input().split()))
        RS.append([num - 1 for num in tmp])
    print(main(A, RS))
