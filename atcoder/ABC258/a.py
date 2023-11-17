# https://atcoder.jp/contests/abc258/tasks/abc258_a

K = int(input())

hour = str((21 * 60 + K) // 60)
minute = str((21 * 60 + K) % 60)

print(f"{hour}:{minute.zfill(2)}")
