# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

# Questions:
# Only ints? 
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent


class BinarySearchTree:
  def __init__(self, value): # We're just using value, so key is value
    self.value = value
    self.left = None
    self.right = None

  # * `insert` adds the input value to the binary search tree, adhering to the
  # rules of the ordering of elements in a binary search tree.
  # Need to traverse to find spot to insert
  def insert(self, value):
    # 1 check if the root exists
        # 2 if not, then assign the input to the root
        # 3 else
          # 4 check if the input is greater than value
            # check if the value exists and repeat 1...4
            # add the input to the self.right
          # 5 if the input is lesser than the value
            # check if the value exists and repeat 1...4
            # add the input to the self.left

    if value >= self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    else:
      if self.left is None:
        self.left = BinarySearchTree(value)           
      else:
        self.left.insert(value)
    

  # * `contains` searches the binary search tree for the input value, 
  # returning a boolean indicating whether the value exists in the tree or not.
  # Start from root and traverse the tree
  # We can stop at the first instance of a value
  # We know it's not found if we get to a node that doesn't have children
  def contains(self, target):
    current_node = self
    flag = True

    while flag:
      if current_node and current_node.value == target:
        return True
      elif current_node and target > current_node.value:
        if self.right and self.right == target:
          return True
        else:
          current_node = current_node.right
          flag = True
        
      elif current_node and target < current_node.value:
        if self.left and self.left == target:
          return True
        else:
          current_node = current_node.left
          flag = True

      else:
        return False
    

  # * `get_max` returns the maximum value in the binary search tree.
  def get_max(self):

    current = self
    maxi = self.value

    if current is None:
      return None
    else:
      while current:
        if current.right:
          if maxi < current.right.value:
            maxi = current.right.value
            current = current.right
        else:
          current = None

      return maxi



  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 
  def for_each(self, cb):
    pass


# bst = BinarySearchTree(5)

# print(bst.insert(2))

# print(bst.insert(3))

# print(bst.insert(7))

# print(bst.get_max())
# print(bst.insert(10))
# print(bst.get_max())
# print(bst.insert(3))
# print(bst.get_max())

# print(bst.contains(8))

# print(f'value is {bst.value}')

# print(f'left value is {bst.left.value}')

# print(f'right value is {bst.right.value}')