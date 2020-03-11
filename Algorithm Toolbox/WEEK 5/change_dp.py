# Uses python3
import sys
def get_change(m):
	dp=[m+1]*(m+1)
	coins=[1,3,4]
	dp[0]=0
	for i in range(0,m+1):
		for j in coins:
			if j<=i:
				dp[i]=min(dp[i],dp[i-j]+1)
	return dp[m]
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
