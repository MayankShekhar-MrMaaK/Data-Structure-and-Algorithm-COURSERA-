#Uses python3

import sys

def lcs2(x: str, y: str):
    assert x is not None
    assert y is not None

    m = len(x)
    n = len(y)

    # declaring the array for storing the dp values
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                match = 1
            else:
                match = 0

            L[i][j] = max(L[i - 1][j], L[i][j - 1], L[i - 1][j - 1] + match)

    seq = ""
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            match = 1
        else:
            match = 0

        if L[i][j] == L[i - 1][j - 1] + match:
            if match == 1:
                seq = x[i - 1] + seq
            i -= 1
            j -= 1
        elif L[i][j] == L[i - 1][j]:
            i -= 1
        else:
            j -= 1
    return seq

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]
    print(lcs2(a, b))