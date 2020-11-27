# 链表表达方式
class Node():
  def __init__(self,value, next=None):
    self.value = value
    self.next = next

L = Node('a', Node('b', Node('c', Node('d'))))
print(L.next.next.value)