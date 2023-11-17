N = int(input())
A = list(map(int, input().split()))
count_operate = 0
isEven = True

while isEven:
    # すべての要素が偶数であるか判定する
    for a in A:
        if a % 2 == 1:
            isEven = False
            break
    for i in range(N):
        A[i] = A[i] / 2
    count_operate += 1
        
print(count_operate - 1)
