import sys
global_counter = 0
def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    return number_of_inversions
def merge_sort(a):
    global global_counter
    if len(a) == 1:
        return a
    mid = len(a) // 2
    j = merge_sort(a[:mid])
    k = merge_sort(a[mid:])
    ans = merge(j, k)
    return ans
def merge(a, b):
    global global_counter
    c = []
    while a and b:
        if a[0] > b[0]:
            c.append(a[0])
            global_counter += len(b)
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
    c = c + a + b
    return c
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    merge_sort(a)
    print(global_counter)