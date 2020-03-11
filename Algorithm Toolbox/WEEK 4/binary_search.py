# Uses python3
import sys

def binary_search(arr,low,high,x):
	if high<low:
		return -1
	mid=low+(high-low)//2
	if x==arr[mid]:
		return mid
	elif x<arr[mid]:
		return binary_search(arr,low,mid-1,x)
	elif x>arr[mid]:
		return binary_search(arr,mid+1,high,x)
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a,0,len(a)-1, x))
