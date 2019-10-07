class Solution: 
  def getRange(self, arr, target):
    index = binary_search(arr, target)
    if index == -1:
      return [-1, -1]
    
    left = right = index

    while left - 1 >= 0 and arr[left - 1] == target:
      left = left - 1

    while right + 1 < len(arr) and arr[right + 1] == target:
      right = right + 1

    return [left, right]

def binary_search(arr, target):
  low = 0
  high = len(arr) - 1

  while low <= high:
    midPoint = (low + high) / 2
    midPoint = int(midPoint)

    current = arr[midPoint]
    if current == target:
      return midPoint
    
    if current < target:
      low = midPoint + 1
    else:
      high = midPoint

  return -1
    
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]