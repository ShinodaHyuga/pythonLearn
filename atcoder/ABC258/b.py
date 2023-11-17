# https://atcoder.jp/contests/abc259/tasks/abc259_b

import numpy as np

a, b, d = map(int, input().split())

a_prime = a * np.cos(d * np.pi / 180) - b * np.sin(d * np.pi / 180)
b_prime = a * np.sin(d * np.pi / 180) + b * np.cos(d * np.pi / 180)

print(a_prime, b_prime)
