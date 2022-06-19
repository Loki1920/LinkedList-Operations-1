#LinkedList operation
class Node():
    def __init__(self,data):
        self.data = data
        self.ref = None
# Traversal    
class LinkedList():
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print("LinkedList is empty:")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end = " ")
                n = n.ref
    # node addition in beginning
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node 
    # add node at end 
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    # Add After the given node 
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n=n.ref
        if n is None:
            print("node is not present in LinkedList")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    #Add Before the given node 
    def add_before(self,data,x):
        if self.head is None:
            print("linkedList is empty")
            return 
        if self.head.data==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node



LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(25)
#add node after given node
LL1.add_after(35,25)
#add node at end 
LL1.add_end(30)
# add before 35
LL1.add_before(33,35)
#add node at beginning
LL1.add_begin(20)
#print linked list
LL1.print_LL()