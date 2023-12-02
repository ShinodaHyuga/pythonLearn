def main(lst: list):
    total_lst = []
    for l in lst:
        t1 = l[0]
        t2 = l[1]
        t3 = 24 - l[2]
        total_t = t1 + t2 + t3
        total_lst.append(total_t)
    return min(total_lst), max(total_lst)
    
if __name__ == "__main__":
    N = int(input())
    lines = []
    for _ in range(N):
        line = list(map(int, input().split()))
        lines.append(line)
    min_, max_ = main(lines)
    print(min_)
    print(max_)

