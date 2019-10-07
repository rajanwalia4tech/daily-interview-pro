class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
  
  # Function to print the list
  def printList(self):
    node = self
    output = '' 
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution
  def reverseIteratively(self, head):
    previous = None
    current = head
    while current:
      temp = current.next 
      if current:
        current.next = previous
        previous = current
        current = temp

  # Recursive Solution      
  def reverseRecursively(self, head):
    previous = None
    self.reverseRecursively_(head, previous)
  
  def reverseRecursively_(self, current, previous):
    if current:
      temp = current.next
      current.next = previous
      previous = current
      current = temp
      self.reverseRecursively_(current, previous)


# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
# testHead.reverseIteratively(testHead)
testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4