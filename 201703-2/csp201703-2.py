# n=int(input())

# dic={}
# for i in range(1,n+1):
# 	dic[i]=i

# m=int(input())
# changes=[]
# for i in range(m):
# 	change=list(map(lambda x: int(x), input().split()))
# 	dic[change[0]]+=change[1]
# 	tem=change[0]+change[1]
# 	b=change[1]<0
# 	if b:
# 		change[0],tem=tem,change[0]
# 	for c in range(change[0],tem): # 不对，这里的c是顺序，但dic的key是学号
# 		dic[c]-=b*2-1

# for i in range(1,n+1):
# 	print(dic[i],end=' ')
# print()

# dic2=[0]
# for i in range(1,n+1):dic2.append(0)
# for i in range(1,n+1):
# 	dic2[dic[i]]=i

# for i in range(1,n+1):
# 	print(dic2[i],end=' ')


n=int(input())
lst=list(range(1,n+1))
m=int(input())
for i in range(m):
	change=list(map(lambda x: int(x), input().split()))
	ix=lst.index(change[0])
	lst.pop(ix)
	lst.insert(ix+change[1],change[0])

for i in range(0,n):
	print(lst[i],end=' ')
	