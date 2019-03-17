from operator import xor
from functools import reduce






def conv(x):
    s = bin(x)[2:]
    res=''
    for i in range(8):
        res+=d1[int(s[4*i:4*i+4], base = 2)]
        
    return res



# begin_initial
lst = [
    ('A',10),
    ('B',11),
    ('C',12),
    ('D',13),
    ('E',14),
    ('F',15),
    ]

    
d1 = {}
d2 = {}
for x in lst:
    d1[x[0]]=x[1]
    d1[x[1]]=x[0]

for i in range(10):
    d1[str(i)] = i
    d1[i] = str(i)


# end_initial

d_disk = {}
n ,s, l = map(int, input().split())
for i in range(l):
    idx, string = input().split()
    d_disk[int(idx)] = string

m = int(input())
for i in range(m):
    b = int(input())
    # nth trip
    idx1 = b // s
    # nth disk
    idx2 = idx1 % n
    
    # nth trip in that disk(not count p)
    idx3 = idx1 // n
    # nth trip in that disk(count p)
    idx3 += (idx3 // (n - 1)) + (idx3 >= (n - idx2 -1))
    
    # nth block in that disk
    idx4 = idx3 * s + b % s
    

    ######
    if d_disk.get(idx2):
        print(d_disk[idx2][idx4*8:idx4*8+8])
    else:
        if l == n - 1:
            
            lst = list(range(n))
            lst.pop(idx2)
            
            nums = [int(d_disk[i][idx4*8:idx4*8+8], base=16) for i in lst]
            print(conv(reduce(xor, nums)))
            
                
                
        else:
            print('-')
    







