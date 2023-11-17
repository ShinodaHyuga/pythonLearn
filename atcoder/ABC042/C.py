#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
C - こだわり者いろはちゃん
https://atcoder.jp/contests/abc042/tasks/arc058_a
"""

N, K = map(int, input().split())
D = list(map(int, input().split()))

for i in range(N, N * 10):
    cnt = 0
    for d in D:
        if str(d) in str(i):
            break
        else:
            cnt += 1
            
    if cnt == len(D):
        print(i)
        break
