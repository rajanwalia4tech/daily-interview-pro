def sortNums(nums):
  # merge sort/ quick sort etc best performance O (n log n)
  # O(n)? counting sort/ radix sort
  # list only will have (1,2,3), counting sort makes sense
  countArr = [0 for _ in range(3)]
  sortArr = []
  for i in nums:  countArr[i-1] += 1
  for i in range(3): sortArr.extend([i+1 for j in range(countArr[i])])
  return sortArr
  

print (sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]