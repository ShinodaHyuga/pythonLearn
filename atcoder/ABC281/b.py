S = str(input())

alfabets, numbers = [], []

for s in S:
    if 65 <= ord(s) <= 90:
        alfabets.append(s)
    elif 48 <= ord(s) <=57:
        numbers.append(s)
    else:
        print("No")
        break

if len(alfabets) == 2 and len(numbers) == 6 and numbers[0] != "0":
    print("Yes")
else:
    print("No")
