cache = [0] * 100
cache[0] = 1
cache[1] = 1

def staircase(n):
    if n <= 1:
        return cache[n]
    else:
        cache[n] = staircase(n-1) + staircase(n-2)
        return cache[n]
  # 1 1 2 3 5 8
  
print staircase(4)
# 5
print staircase(5)
# 8