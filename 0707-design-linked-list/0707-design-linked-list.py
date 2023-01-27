class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
    

class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        if not self.head:
            return -1
        curr = 0
        temp_node = self.head
        
        while temp_node:
            if curr == index:
                return temp_node.val
            curr += 1
            temp_node = temp_node.next
        
        return -1
               
        
        """
        :type index: int
        :rtype: int
        """
        

    def addAtHead(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        """
        :type val: int
        :rtype: None
        """
        

    def addAtTail(self, val):
        new_node = Node(val)
        temp = self.head
        if not self.head:
            self.head = new_node
            return
        while temp.next:
            temp = temp.next
        temp.next = new_node
            
        """
        :type val: int
        :rtype: None
        """
        

    def addAtIndex(self, index, val):
        curr = 0
        temp = self.head
        new_node = Node(val)
        if index == 0:
            self.addAtHead(val)
            return
        while temp:
            if curr == index - 1:
                new_node.next = temp.next
                temp.next = new_node
                return
            curr += 1
            temp = temp.next
                
        
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def deleteAtIndex(self, index):
        curr = 0
        temp = self.head
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        while temp:
            if curr == index - 1:
                if temp.next:
                    if temp.next.next:
                        temp.next = temp.next.next
                    else:
                        temp.next = None
                else:
                    temp.next = None
                return
            curr += 1
            temp = temp.next
        """
        :type index: int
        :rtype: None
        """
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)