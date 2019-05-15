class Node:
  def __init__(self, value = None, next_node = None):
    # the value at this linked list Node
    self.value = value
    # refernce tot he next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next_node):
    self.next_node = new_next_node

class LinkedList:
  def __init__(self):
    #reference to the head of the list
    self.head = None
    #reference to the tail of the list
    self.tail = None

  def add_to_tail(self, value):
    # init a node with a value of ValueError
    new_node = Node(value, None)
    # check if there is no head( i.e list is empty)
    if self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      #set the current tails next reference to our new node
      self.tail.set_next(new_node)
      self.tail = new_node  
    
  def remove_head(self):
    # Return none if there is no head
    if self.head is None:
      return None
    # Check to see if there is only one element
    elif not self.head.get_next():
      head = self.head
      self.head = None
      self.tail = None
      return head.get_value()
    else:
      value = self.head
      self.head = self.head.get_next()
      return value.get_value()

  def contains(self, value):
    # if list of empty
    if not self.head:
      return False

    else:
      current = self.head
      while current:
        if value == current.get_value():
          return True
        else:
          current = current.get_next()

    return False

  def add_to_head(self, value):
    # inti node wth value of ValueError
    new_node = Node(value, None)
    # If list is empty
    if not self.head:
      self.head = new_node
      self.tail = new_node
    # If list only has one item
    elif not self.head.get_next():
      new_node.set_next = self.head
      self.head = new_node
      
    else:
      prev_head = self.head
      self.head = new_node
      self.head.set_next(prev_head)

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    self.size += 1
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    if self.size == 0:
      return None
    else:
      self.size -= 1
      return self.storage.remove_head()

  def len(self):
    return self.size
     