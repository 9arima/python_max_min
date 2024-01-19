#findig minimum and maximum from list
nums=[5,15,20]
max1=nums[0]
for ele in nums:
    if ele>max1:
        max1=ele
print("maximum value is:",max1)

min1=nums[0]
for ele in nums:
    if ele>min1:
        min1=ele
print("minimum value is:",min1)