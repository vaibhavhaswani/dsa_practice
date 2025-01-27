class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def enqueue(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        if self.tail is None:
            self.head.next=node
            self.tail=node
            return

        self.tail.next=node
        self.tail=node
        

    def dequeue(self):
        if self.head is None:
            return None
        data=self.head.data
        self.head=self.head.next
        return data

    def peek(self):
        return self.head.data

    def isempty(self):
        return self.head is None
    
    def display(self):
        temp_head=self.head
        print("Your List:", end=" ")
        while temp_head:
            print(temp_head.data,end=" > ")
            temp_head=temp_head.next
        print()
    

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)

queue.display()

queue.enqueue(30)

print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
