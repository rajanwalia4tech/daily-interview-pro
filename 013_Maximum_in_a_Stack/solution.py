class MaxStack:
  def __init__(self):
    pass

  def push(self, val):
    pass

  def pop(self):
    pass

  def max(self):
    pass

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print s.max()
# 3
s.pop()
s.pop()
s.pop()
s.pop()
print s.max()
# 2