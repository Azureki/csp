
'''
读取每一行
保存入dict
key是时间，val是教室

然后再用list
遍历dict
'''


# N,K=tuple(map(lambda x: int(x), input().split())) # 总教室数，今天上课教师数
N,K=map(lambda x: int(x), input().split())
d1={} # 开始时间
d2={} # 归还时间
time=set() # 所有时间节点
box=list(range(1,N+1)) # 盒子,如果为0则被借走，有数，则存的是钥匙号
pos=[0]+list(range(N)) # 位置 index是号，val是存放的位置

for i in range(K):
	room,start,length=map(lambda x: int(x), input().split())
	if not d1.get(start):
		d1[start]=[]
		time.add(start)
	d1[start].append(room)

	end=start+length
	if not d2.get(end):
		d2[end]=[]
		time.add(end)
	d2[end].append(room)
	
time_list=sorted(time)

for t in time_list:
	# 先还再借
	if d2.get(t):
		d2[t].sort()
		idx=0
		for r in d2[t]:
			for i in range(idx,N):
				if box[i]!=0:
					continue
				else:
					box[i]=r
					pos[r]=i
					idx=i+1
					break

	if d1.get(t):
		for r in d1[t]:
			box[pos[r]]=0

for i in box:
	print(i,end=' ')
