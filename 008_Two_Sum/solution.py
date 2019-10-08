def two_sum(nums, k):
    seen = set()
    for num in nums:
        diff = k - num
        if diff in seen:
            return True
        seen.add(num)
    return False

print (two_sum([4,7,1,-3,2], 5))
# True