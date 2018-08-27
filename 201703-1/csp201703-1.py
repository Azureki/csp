n,k=map(lambda x: int(x), input().split())
cakes=list(map(lambda x: int(x), input().split()))
friends=0
tem=0
for i in range(n):
	tem+=cakes[i]
	if tem<k:
		if i ==n-1:
			friends+=1
		continue
	else:
		tem=0
		friends+=1

print(friends)
