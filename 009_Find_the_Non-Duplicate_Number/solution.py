def singleNumber(nums):
    nums.sort()
    previous = nums[0]
    count = 1
    for i in range(len(nums)-1):
        if nums[i+1] == previous:
            count += 1
        elif nums[i+1] != previous:
            if count != 2:
                return previous
            else:
                count = 1
                previous = nums[i+1]
    return previous

print (singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1