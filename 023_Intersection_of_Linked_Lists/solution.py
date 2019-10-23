def intersection(a, b):
    # fill this in
    current = Node(0)
    c = current
    b_ = b
    while a:
        b = b_
        while b:
            if a.val == b.val:
                current.val = a.val
                if a.next and b.next: 
                    a = a.next 
                    b = b.next
                else:
                    return c

                current.next = Node(0)
                current = current.next
                
                while True:
                    if a.val == b.val:
                        current.val = a.val
                        if a.next and b.next:
                            a = a.next 
                            b = b.next
                        else:
                            return c
                        current.next = Node(0)
                        current = current.next
            b = b.next
        a = a.next
    return c

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
  def prettyPrint(self):
    c = self
    while c:
      print c.val,
      c = c.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()
# 3 4