# https://atcoder.jp/contests/abc045/tasks/abc045_b
s_a = str(input())
s_a = [a for a in s_a]

s_b = str(input())
s_b = [b for b in s_b]

s_c = str(input())
s_c = [c for c in s_c]

removed = "a"
while True:
    if removed == "a":
        if (len(s_a) == 0):
            print("A")
            exit()
        else:
            removed = s_a.pop(0)
    elif removed == "b":
        if (len(s_b) == 0):
            print("B")
            exit()
        else:
            removed = s_b.pop(0)
    else:
        if (len(s_c) == 0):
            print("C")
            exit()
        else:
            removed = s_c.pop(0)
