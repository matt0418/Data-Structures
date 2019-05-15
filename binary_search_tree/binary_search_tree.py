class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

    elif value >= self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == None:
      return False
    elif target == self.value:
      return True
    elif target < self.value and self.left:
      return self.left.contains(target)
    elif target > self.value and self.right:
      return self.right.contains(target)
    else:
      return False

  def get_max(self):
    if self.value == None:
      return None
    max = 0
    current = self
    while current:
      if current.value > max:
        max = current.value
      current = current.right
    return max

  def for_each(self, cb):
    self.value = cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)