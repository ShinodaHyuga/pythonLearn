input_line = input()
line = []
hoge = {"A": 4, "E": 3, "G": 6, "I": 1, "O": 0, "S": 5, "Z": 2}
for i in range(len(input_line)):
    if input_line[i] in hoge:
        line.append(hoge[input_line[i]])
    else:
        line.append(input_line[i])
    print(line[i], end = "")
