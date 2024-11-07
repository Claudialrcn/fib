import argparse
import sys


def fibonacci_iterative(n: int) -> int:
    """
    Computes the n-th Fibonacci number.
    :param n: n-th fibonacci number
    :return: the n-th fibonacci number
    """
    if n < 0:
        raise ValueError("n must be greater or equal to zero.")
    if n < 2:
        return n

    n0 = 0
    n1 = 1
    for _ in range(n):  ## _ cuando no usamos la variable del bucle
        nth = n1 + n0
        n0 = n1
        n1 = nth
    return n0


cache = {}


def fibonacci_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n must be greater or equal to zero.")
    if n < 2:
        return n
    ##Esto es para darle velocidad al codigo, guardando numeros que ya ayamos calculado para no volver a hacerlo
    if n in cache:
        return cache[n]
    nth = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    cache[n] = nth
    return nth


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Fibonacci',
        description='Gives the nth Fibonacci number')

    parser.add_argument('nth', type=int, help="Nth Fibonacci number.")

    args = parser.parse_args()
    result = fibonacci_recursive(args.nth)
    print(result)

    # n = int(args[1])
    # result = fibonacci_iterative(n)
    ##print(result)
