class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

  def print(self):
    print(self.data)

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)

    if not self.head:
      self.head = new_node
    else:
      curr = self.head
      while curr.next:
        curr = curr.next

      curr.next = new_node

  def print(self):
    curr = self.head

    while curr:
      curr.print()
      curr = curr.next


if __name__ == '__main__':
  l = LinkedList()
  l.append(1)
  l.append(2)
  l.append(3)
  l.print()
