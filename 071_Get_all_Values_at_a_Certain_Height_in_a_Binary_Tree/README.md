# Get all Values at Certain Height in a Binary Tree
Hi, here's your problem today. This problem was recently asked by Amazon:

By the way, check out our NEW project AlgoPro (http://algopro.com) for over 60+ video coding sessions with ex-Google/ex-Facebook engineers.

Given a binary tree, return all values given a certain height h.

Here's a starting point:
```
class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):
  # Fill this in.

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print valuesAtHeight(a, 3)
# [4, 5, 7]
```