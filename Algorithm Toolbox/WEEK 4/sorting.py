# Uses python3
import sys
import random
def randomized_quick_sort(arr,l,r):
    if l >= r:
        return
    k = random.randint(l, r)
    arr[l], arr[k] = arr[k], arr[l]
    m, n = partition(arr, l, r)
    randomized_quick_sort(arr,l,m-n)
    randomized_quick_sort(arr,m+1,r)
def partition(arr,l,r):
    pivot = arr[l]
    j,k,m=l,1,0
    for i in range(l + 1, r + 1):
        if arr[i] < pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
        elif arr[i] == pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[j], arr[l + k] = arr[l + k], arr[j]
            k += 1
    while m < k:
        arr[l + m], arr[j - m] = arr[j - m], arr[l + m]
        m += 1
    return j, m
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
