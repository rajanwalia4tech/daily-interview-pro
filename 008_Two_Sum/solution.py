def two_sum(nums, k):
    seen = set()
    for num in nums:
        seen.add(num)
        diff = k - num
        if diff in seen:
            return True
    return False

print (two_sum([4,7,1,-3,2], 5))
# True