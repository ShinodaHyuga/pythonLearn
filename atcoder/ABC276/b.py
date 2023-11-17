# https://atcoder.jp/contests/abc276/tasks/abc276_b

N, M = map(int, input().split())
empty_lst = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())

    empty_lst[A - 1].append(B)
    empty_lst[B - 1].append(A)

print("=" * 32)

for lst in empty_lst:
    lst.sort()
    lst_str = [str(l) for l in lst]  # 出力のために変数をstr型にした変数を用意
    print(len(lst_str), " ".join(lst_str))
    # print(len(lst_str), *lst) # こっちの方がスマート
