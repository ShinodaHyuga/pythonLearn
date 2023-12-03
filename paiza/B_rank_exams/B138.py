def main(H, W, S):
    ans = 0
    for h in range(H - 2):
        for w in range(W - 2):
            top_line_is_donut    = S[h][w] == S[h][w + 1] == S[h][w + 2] == "#"
            middle_line_is_donut = S[h + 1][w + 0] == S[h + 1][w + 2] == "#" and S[h + 1][w + 1] == "."
            bottom_line_is_donut = S[h + 2][w + 0] == S[h + 2][w + 1] == S[h + 2][w + 2] == "#"
            if top_line_is_donut and middle_line_is_donut and bottom_line_is_donut:
                ans += 1
    return ans

if __name__ == "__main__":
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append([s for s in str(input())])
    print(main(H, W, S))
