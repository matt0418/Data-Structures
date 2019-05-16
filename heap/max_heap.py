class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    if len(self.storage) == 0:
      return None
    elif len(self.storage) == 1:
      return self.storage.pop()
    else:
      item = self.storage[0]
      self.storage[0] = self.storage[len(self.storage)-1]
      self.storage.pop()
      self._sift_down(0)
      return item
    

  def get_max(self):
    if self.storage[0] == None:
      return None
    else:
      return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # loop over array until element reaches top of array or break when elements priority is not greater then parents value
    while index > 0:
      p = (index-1)//2
      if self.storage[index] > self.storage[p]:
        #swap elements
        self.storage[index], self.storage[p] = self.storage[p], self.storage[index]
        #update index
        index = p
      else:
        break

  def _sift_down(self, index):
    left = (2*index) + 1
    right = (2*index) + 2
    greatest = index
    if len(self.storage) > left and self.storage[greatest] < self.storage[left]:
      greatest = left
    if len(self.storage) > right and self.storage[greatest] < self.storage[right]:
      greatest = right
    if greatest == index:
      return
    else:
      self.storage[index], self.storage[greatest] = self.storage[greatest], self.storage[index]
      self._sift_down(greatest)
