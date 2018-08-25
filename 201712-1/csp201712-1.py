# read data
n=int(input())
nums=[int(x) for x in input().split()]

nums.sort()
print(min(abs(nums[i]-nums[i-1])  for i in range(1,n)))