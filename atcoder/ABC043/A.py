"""
A - キャンディーとN人の子供イージー
https://atcoder.jp/contests/abc043/tasks/abc043_a
"""

def main():
    N = int(input())
    result = 0
    for i in range(1, N + 1):
        result += i
    print(result)
    
if __name__ == "__main__":
    main()
