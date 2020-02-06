# Uses python3
import sys

def fib_fast(n):
    if n == 0:
        return 0
    n = n + 2
    a = [0, 1]
    while True:
        a.append((a[-1]+a[-2]) % 10)
        if a[-1] == 1 and a[-2] == 0:
            a.pop()
            a.pop()
            break
    z = a[n % len(a)] - 1
    return z if z != -1 else 9

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_fast(n))
