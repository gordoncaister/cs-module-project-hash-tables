
class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    

class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
    
    def put(self, data):
        new_node = Node(data)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def get(self,data):
        if not self.head:
            return
        current = self.head
        while current is not None:
            if current.value.key == data:
                return current.value