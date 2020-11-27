#将列表转换成链表
# 初始化一个链表类型
class LinkedNode(object):
    def __init__(self,val = None,next = None):
        self.val = val
        self.next = next


def list_to_linkNode(array):
    tmp_node = LinkedNode()
    node = LinkedNode()
    for i in array:
        if not tmp_node.val:
            tmp_node.val = i
            node = tmp_node
        else:
            tmp_node.next = LinkedNode(i)
            tmp_node = tmp_node.next
    return node

if __name__ == '__main__':
    array = [1,2,3,4,5]
    print(list_to_linkNode(array).val)
    print(list_to_linkNode(array).next.val)  
    print(list_to_linkNode(array).next.next.val)    