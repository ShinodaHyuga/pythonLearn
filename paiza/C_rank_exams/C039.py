def main(E):
    ans = 0
    for e in E:
        if e == "/":
            ans += 1
        elif e == "<":
            ans += 10
    return ans

if __name__ == "__main__":
    E = str(input())
    print(main(E))
