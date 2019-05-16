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
