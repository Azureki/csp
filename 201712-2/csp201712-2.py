class Node(object):
	def __init__(self, val):
		self.val=val
		self.next=None
		
# read data
n,k=tuple(int(x) for x in input().split())

# init nodes
head=Node(0)
p=head
for i in range(1,n+1):
	p.next=Node(i)
	p=p.next
p.next=head.next

if k==1:
	print(n)

# del
else:
	cnt=1
	p=head
	for i in range(n-1):
		# for step in range(1,k):
		while True:
			if cnt%10==k or cnt%k==0:
				break
			# if (i*k+step)%10==k:
			cnt+=1
			p=p.next
			if cnt%10==k or cnt%k==0:
				break
			# cnt+=1
		tem=p.next
		p.next=tem.next
		# print('cnt=',cnt)
		# print(tem.val)
		cnt+=1

	print(p.next.val)
