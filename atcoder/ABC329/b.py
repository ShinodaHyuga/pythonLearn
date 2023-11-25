def main(n: int, a: list) -> int:
    a = set(a)
    a.remove(max(a))
    return max(a)

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(main(N, A))
