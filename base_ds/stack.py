class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
class Stack:

    def __init__(self):
        self.head=None
        self.tail=None

    
    def push(self,data):
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
        self.tail=node


    def pop(self):
        if self.head is None:
            return "Stack Empty"
        if self.tail is self.head:
            if self.head:
                item=self.head.data
                self.head=None
                return item
            return "Stack Empty"
        item=self.tail.data
        self.tail=self.tail.prev
        self.tail.next=None
        return item
    
    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def display(self):
        temp_head=self.head
        print("Your List:", end=" ")
        while temp_head:
            print(temp_head.data,end=" > ")
            temp_head=temp_head.next
        print()


if __name__=="__main__":
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.display()
    print(stack.pop())
    stack.display()
    print(stack.isempty())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    stack.display()