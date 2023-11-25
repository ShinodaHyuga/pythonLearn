# エラトステネスの篩

import timeit
import numpy as np

def main(max_num: int) -> np.array:
    numbers = np.array(range(2, max_num + 1))
    primes = []
    
    while len(numbers) > 0:
        prime = numbers[0]
        primes.append(prime)
        numbers = rm_multiples(numbers, prime)
    return primes

def rm_multiples(numbers: np.array, value: int) -> np.array:
    rm_idx = np.where(numbers % value == 0)
    return np.delete(numbers, rm_idx)


def main2(max_num: int) -> list:
    numbers = list(range(2, max_num + 1))
    primes = []

    while numbers:
        prime = numbers[0]
        primes.append(prime)
        numbers = rm_multiples2(numbers, prime)

    return primes

def rm_multiples2(numbers: list, value: int) -> list:
    return [num for num in numbers if num % value != 0]


if __name__ == "__main__":
    N = int(input())
    print(main(max_num=N))
    # print(f"use numpy: {timeit.timeit(lambda: main(N), number=1):.4f} s")
    