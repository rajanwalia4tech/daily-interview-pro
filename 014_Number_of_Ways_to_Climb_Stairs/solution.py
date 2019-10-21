def staircase(n):
    if n == 1 or n == 2:
        return n
    else:
        return staircase(n-1) + staircase(n-2)
  # 1 1 2 3 5 8
  
print staircase(4)
# 5
print staircase(5)
# 8