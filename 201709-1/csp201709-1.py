from functools import lru_cache


@lru_cache(None)
def dp(N):
	if N<3:
		return N
	elif N<5:
		return N+1
	

	return max(3+1+dp(N-3),5+2+dp(N-5))

N=int(input())

N=int(N/10)
print(dp(N))