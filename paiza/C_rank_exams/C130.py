def main(AB):
    print(sum([1 for ab in AB if not(ab[0] == ab[1] == "y")]))
    for i, ab in enumerate(AB):
        if not(ab[0] == ab[1] == "y"):
            print(i + 1)

if __name__ == "__main__":
    N = int(input())
    AB = []
    for _ in range(N):
        AB.append(list(map(str, input().split())))
    main(AB)
