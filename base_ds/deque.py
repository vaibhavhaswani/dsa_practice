class Deque:

    def __init__(self):
        self.q=[]

    def isEmpty(self):
        return len(self.q)==0
    
    def __len__(self):
        return len(self.q)
    
    def size(self):
        return len(self.q)
    
    def addFront(self,data):
        self.q.insert(0,data)
        print(f"Data {data} added to Front")

    def addRear(self,data):
        self.q.append(data)
        print(f"Data {data} added to Rear")

    def removeFront(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return None
        data=self.q.pop(0)
        print(f"Data {data} removed from Front")
        return data
    
    def removeRear(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return None
        data=self.q.pop()
        print(f"Data {data} removed from Rear")
        return data
    
    def display(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return
        print("| ".join([str(i) for i in self.q]))

if __name__=="__main__":
    # Example usage
    deque = Deque()

    # Adding elements
    deque.addFront(10)
    deque.addRear(20)
    deque.addFront(5)
    deque.addRear(25)

    # Display the deque
    deque.display()

    # Peek elements
    # print("Front element:", deque.peekFront())
    # print("Rear element:", deque.peekRear())

    # Removing elements
    deque.removeFront()
    deque.removeRear()

    # Display the deque
    deque.display()

    # Check size
    print("Size of deque:", deque.size())