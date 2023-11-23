def main(n: int, s: str) -> str:
    for i in range(1, n):
        if (s[i - 1] == "a" and s[i] == "b") or (s[i - 1] == "b" and s[i] == "a"):
            return "Yes"
    return "No"

if __name__ == "__main__":
    N = int(input())
    S = str(input())
    print(main(N, S))
