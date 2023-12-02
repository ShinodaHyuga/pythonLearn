def main(F):
    ans = 0
    for i in range(1, N + 1):
        ans += abs(F[i] - F[i - 1])
    return ans
    
if __name__ == "__main__":
    N = int(input())
    F = [1]
    for _ in range(N):
        F.append(int(input()))
    print(main(F))
