def main(A, B):
    result = [0 for _ in range(len(A))]
    a_i = 0
    b_i = 0
    while True:
        # このゴンドラに全員が乗れる時
        if A[a_i] >= B[b_i]:
            result[a_i] += B[b_i]
            B[b_i] = 0
            b_i += 1
        # 全員が乗れない時
        else:
            result[a_i] += A[a_i]
            B[b_i] -= A[a_i]
        a_i = (a_i + 1) % len(A)
        b_i %= len(B)
        
        # 客がいなくなったら終了する
        if sum(B) < 1:
            return result

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(int(input()))
    B = []
    for _ in range(M):
        B.append(int(input()))
        
    result = main(A, B)
    for res in result:
        print(res)
