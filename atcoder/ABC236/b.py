N, A, B = map(int, input().split())
for i in range(N):
    for _ in range(A):
        hoge = ""
        if i % 2 == 0:
            for j in range(N):
                if j % 2 == 0:
                    hoge += "." * B
                else:
                    hoge += "#" * B
        else:
            for j in range(N):
                if j % 2 == 0:
                    hoge += "#" * B
                else:
                    hoge += "." * B
        print(hoge)