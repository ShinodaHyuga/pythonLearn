import math

def main(b: int) -> int:
    if b == 1:
        return 1

    for i in range(2, math.sqrt(b) + 1):
        if i ** i == b:
            return i
        if i ** i > b:
            return -1

    return -1

if __name__ == "__main__":
    B = int(input())
    print(main(B))
