import sys
import math
def minimum_distance(points):
    def distance(a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    if len(points) == 1:
        return float('inf')
    elif len(points) == 2:
        return distance(points[0], points[1])
    mid = len(points) // 2
    left_min = minimum_distance(points[:mid])
    right_min = minimum_distance(points[mid:])
    minimum = min(left_min, right_min)
    mid_left, mid_right = [], [points[mid]]
    if left_min != float('inf'):
        shift = 1
        while shift <= mid:
            try:
                if points[mid][0] - points[mid-shift][0] < minimum:
                    mid_left.append(points[mid-shift])
                    shift += 1
                else:
                    break
            except IndexError:
                break
    else:
        mid_left.append(points[mid-1])

    if right_min != float('inf'):
        shift = 1
        while shift <= mid:
            try:
                if points[mid][0] - points[mid+shift][0] < minimum:
                    mid_right.append(points[mid+shift])
                    shift += 1
                else:
                    break
            except IndexError:
                break
    k = float('inf')
    for i in mid_left:
        for j in mid_right:
            s = distance(i, j)
            if s < k:
                k = s
    return min(left_min, right_min, k)
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = sorted([(i, j) for i, j in zip(x, y)], key=lambda x: x[0])
    print("{0:.9f}".format(minimum_distance(points)))