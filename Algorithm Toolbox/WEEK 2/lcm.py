# Uses python3
import sys

def lcm_naive(a, b):
    if a==0 and b==0:
        return 0
    return int(abs((a*b))/gcd(a,b))
def gcd(a, b):
    if b==0:
        return a
    r=a%b
    return gcd(b,r)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))