# Uses python3
import sys

def fib_fast(n):
    a = [0, 1]
    while True:
        a.append((a[-1]+a[-2]) % 10)
        if a[-1] == 1 and a[-2] == 0:
            a.pop()
            a.pop()
            break
    return a[n % len(a)]
def fib_fix(n, m):
    a = fib_fast(m + 2) - fib_fast(n + 1)
    return a if a >= 0 else 10 + a

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fib_fix(n,m))