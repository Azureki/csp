n = int(input())
nums = list(map(int,input().split()))
ma = max(nums[0], nums[-1])
mi = min(nums[0], nums[-1])
mid = nums[len(nums)//2]
if len(nums)%2==0:
    mid += nums[len(nums)//2-1]
    if mid %2 == 0:
        mid = mid//2
        
        print("%d %d %d"%(ma,mid,mi))
    else:
        mid = mid /2
        print("%d %.1f %d"%(ma,mid,mi))

else:
    print("%d %d %d"%(ma,mid,mi))
