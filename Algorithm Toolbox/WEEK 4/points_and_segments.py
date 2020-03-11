import sys
from itertools import chain


def fast_count(starts, ends, points):
    cnt = [0] * len(points)
    zip_starts = zip(['a'] * len(starts), starts)
    zip_ends = zip(['z'] * len(ends), ends)
    zip_points = zip(['x'] * len(points), points, range(len(points)))
    line = chain(zip_starts, zip_ends, zip_points)
    line = sorted(line, key=lambda x: (x[1], x[0]))
    sweeper = 0
    for i in line:
        if i[0] == 'a':
            sweeper += 1
        elif i[0] == 'z':
            sweeper -= 1
        else:
            cnt[i[2]] = sweeper
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = fast_count(starts, ends, points)
    for x in cnt:
        print(x, end=' ')