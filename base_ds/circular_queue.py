## Memory Efficient Queue

class CircularQueue:

    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1

    def isfull(self):
        return (self.rear+1)%self.size==self.front
    
    def isempty(self):
        return self.front==-1

    def enqueue(self,data):
        if self.isfull():
            print(f"Queue Full | cannont insert data : {data}")
            return
        if self.isempty():
            self.front = 0 # set front to start
        self.rear=(self.rear+1)%self.size #make rear dynamic to circular motion as when self.rear =4 , the self.rear will become 0
        self.queue[self.rear]=data
        print("Data Enqueued:",data)

    def dequeue(self):
        if self.isempty():
            print("Queue is Empty!")
            return None
        data=self.queue[self.front]
        self.queue[self.front]=None
        if self.rear==self.front: ##if queue becomes empty after dequeueing reset queue
            self.rear=-1
            self.front=-1
        else:
            self.front=(self.front+1)%self.size
        return data
        

    def display(self):
        if self.isempty():
            print("Empty Queue")
            return
        if self.rear>=self.front:
            for i in self.queue[self.front:self.rear+1]:
                print(f"{i}",end=" > ")
        else:
            for i in self.queue[self.front:]:
                print(f"{i}",end=" > ")
            for i in self.queue[:self.rear+1]:
                print(f"{i}",end=" > ")
        print()

    def queuestate(self):
        print("| ".join([str(i) for i in self.queue]))

if __name__=="__main__":
    # Example usage
    cq = CircularQueue(5)  # Create a circular queue of size 5

    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.enqueue(50)  # Queue is now full
    cq.display()

    
    cq.dequeue()  # Removes 10
    cq.dequeue()  # Removes 20
    cq.display()
    cq.queuestate()
    cq.enqueue(60)  # Adds 60
    cq.queuestate()
    cq.enqueue(70)  # Adds 70 (wraps around)
    cq.display()
    cq.queuestate()