# Uses python3
import sys
def get_change(m):
	deno=[1,5,10]
	ans=[]
	i=len(deno)
	i=len(deno)-1
	while(i >= 0):
		while(m>=deno[i]):
			m-=deno[i]
			ans.append(deno[i])
		i-=1
	return len(ans)
	# return (m//10)+(m%10)//5+(m%10)%5
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
