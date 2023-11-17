#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A - 和風いろはちゃんイージー
https://atcoder.jp/contests/abc042/tasks/abc042_a
"""

N, L = map(str, input().split())
S = []
for _ in range(int(N)):
    S.append(str(input()))
S.sort()
print("".join(S))
