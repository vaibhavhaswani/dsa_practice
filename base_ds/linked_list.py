class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyList:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        assert data is not None, "Invalid Data"
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        tail=self.head
        while tail.next:
            tail=tail.next
        tail.next=new_node

    def prepend(self,data):
        assert data is not None, "Invalid Data"
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def delete(self,key):
        head_clone=self.head
        if head_clone.data==key:
            self.head=head_clone.next
            return
        while head_clone.next is not None and head_clone.next.data!=key:
            head_clone=head_clone.next

        assert head_clone.next is not None, "No such value found"

        head_clone.next=head_clone.next.next
    
    def display(self):
        temp_head=self.head
        print("Your List:", end=" ")
        while temp_head:
            print(temp_head.data,end=" > ")
            temp_head=temp_head.next
        print()

if __name__=="__main__":
    sls=SinglyList()
    sls.display()
    sls.insert(123)
    sls.insert(1000)
    sls.insert(540)
    sls.display()
    sls.prepend(0)
    sls.display()
    sls.delete(0)
    sls.display()
    sls.delete(111)
    sls.display()




        
        