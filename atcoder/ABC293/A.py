S = str(input())
result = ""

for i in range(int(len(S) / 2)):
    s1 = S[2 * i]
    s2 = S[2 * i + 1]
    result += s2 + s1

print(result)
