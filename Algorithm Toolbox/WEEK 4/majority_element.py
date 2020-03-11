# Uses python3
import sys
def get_majority_element(arr,low,size):
    m={}
    for i in range(size):
        if arr[i] in m:
            m[arr[i]]+=1
        else:
            m[arr[i]]=1
    count=0
    for key in m:
        if m[key]>size//2:
            count=1
            break
    if count==1:
        return 1
    else:
        return 0
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a, 0, n))
