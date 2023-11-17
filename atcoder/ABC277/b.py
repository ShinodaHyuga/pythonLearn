# https://atcoder.jp/contests/abc277/

N = int(input())
Ss = []

for _ in range(N):
    Ss.append(str(input()))

suits = ["H", "D", "C", "S"]                                             # トランプの柄.
numbers = ["A"] + [str(n) for n in range(2, 10)] + ["T", "J", "Q", "K"]  # トランプの数字.

for i in range(N):
    # 条件1の判定.
    if Ss[i][0] not in suits:
        exists = False
        break
    # 条件2の判定.
    elif Ss[i][1] not in numbers:
        exits = False
        break
    # これら以外のカードは存在.
    else:
        exists = True

# 条件3の判定.
overlapping = N != len(list(set(Ss)))

# すべてのカードが存在し重複がない時にYes, それ以外でNo.
print("Yes" if (exists and not overlapping) else "No")
