#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
B - 文字列大好きいろはちゃんイージー
https://atcoder.jp/contests/abc042/tasks/abc042_b
"""

A, B, C = map(int, input().split())

if A == 7:
    if B == C == 5:
        print("YES")
    else:
        print("NO")
elif B == 7:
    if C == A == 5:
        print("YES")
    else:
        print("NO")
elif C == 7:
    if A == B == 5:
        print("YES")
    else:
        print("NO")
    