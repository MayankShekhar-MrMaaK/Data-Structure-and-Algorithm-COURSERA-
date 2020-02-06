# Uses python3
n = int(input())
def calc_fib(n):
	if n<=1:
		return n
	f=[0]*(n+1)
	f[0]=0
	f[1]=1
	for i in range(2,n+1):
		f[i]=(f[i-1]+f[i-2])
	return (f[n])
print(calc_fib(n))
