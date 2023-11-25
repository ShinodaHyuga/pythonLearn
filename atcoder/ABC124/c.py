def main(lst: list) -> int:
    prev_n = lst[0]
    reverse_cnt = 0
    for i in range(1, len(lst)):
        curt_n = lst[i]
        if prev_n == curt_n:
            prev_n = 1 if curt_n == 0 else 0
            reverse_cnt += 1
        else:
            prev_n = curt_n
    return reverse_cnt

if __name__ == "__main__":
    S = str(input())
    print(main(lst=[int(s) for s in S]))
