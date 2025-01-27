class PriorityQueue:

    def __init__(self):
        self.queue=[]

    def isempty(self):
        return len(self.queue)==0
    
    def enqueue(self,value,priority):
        self.queue.append((priority,value))
        self.queue.sort(key=lambda x:x[0])
        print(f"Enqueued Item {value} with priority {priority}")
    
    def dequeue(self):
        if self.isempty():
            print("Queueu is Empty")
            return None
        element=self.queue.pop(0)
        print(f"Data of value {element[1]} with priority {element[0]} is dequeued !")
        return element[1]
    
    def display(self):
        if self.isempty():
            print("Queueu is Empty")
        else:
            print("| ".join([str(i[1]) for i in self.queue]))

if __name__=="__main__":
    # Example usage
    pq = PriorityQueue()
    pq.enqueue("Task A", 2)
    pq.enqueue("Task B", 5)
    pq.enqueue("Task C", 1)
    pq.enqueue("Task D", 3)

    pq.display()
    # print("Peek:", pq.peek())

    pq.dequeue()
    pq.dequeue()

    pq.display()


