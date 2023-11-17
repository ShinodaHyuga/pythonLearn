N = int(input())
lst = [[1]]
for i in range(1, N):
    tmp = [1]
    if i > 1:
        for j in range(1, i):
            tmp.append(lst[i - 1][j - 1] + lst[i - 1][j])
    tmp.append(1)
    lst.append(tmp)

for i in range(len(lst)):
    for j in lst[i]:
        print(j, " ", end="")
    print()
