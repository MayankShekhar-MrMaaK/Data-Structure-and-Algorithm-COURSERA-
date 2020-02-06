# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    a = [0, 1]
    while True:
        a.append((a[-1]+a[-2]) % m)
        if a[-1] == 1 and a[-2] == 0:
            a.pop()
            a.pop()
            break
    return a[n % len(a)]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
