from functools import cache
from typing import Iterable


@cache
def fib(n: int) -> int:
    print(fib.cache_info())
    return n if n <= 1 else fib(n-1) + fib(n-2)

def fibg(n: int) -> Iterable[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    # print(list(fibg(100)))
    n = int(input('enter n: '))
    print(list(fibg(n))[-1])