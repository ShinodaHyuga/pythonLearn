def main(s: str) -> list:
    return list(map(str, s))

if __name__ == "__main__":
    S = str(input())
    print(*main(S))
