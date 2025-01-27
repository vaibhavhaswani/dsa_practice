class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyList:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        assert data is not None, "Invalid Data"
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        tnode=self.head
        while tnode.next:
            tnode=tnode.next
        tnode.next=node
        node.prev=tnode

    
    def prepend(self,data):
        assert data is not None, "Invalid Data"
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        node.next=self.head
        self.head.prev=node

    def delete(self,key):
        tnode=self.head
        if tnode.data==key:
            self.head=tnode.next
            tnode.prev=None
            return

        while tnode.next!=None and tnode.next.data!=key:
            tnode=tnode.next

        assert tnode.next is not None, "No such data in List"

        nxtnode=tnode.next.next
        tnode.next=nxtnode
        nxtnode.prev=tnode
    

    def display(self):
        temp_head=self.head
        print("Your List:", end=" ")
        while temp_head:
            print(temp_head.data,end=" > ")
            temp_head=temp_head.next
        print()

if __name__=="__main__":
    dls=DoublyList()
    dls.display()
    dls.insert(123)
    dls.insert(1000)
    dls.insert(540)
    dls.display()
    dls.prepend(0)
    dls.display()
    dls.delete(0)
    dls.display()
    dls.delete(111)
    dls.display()

