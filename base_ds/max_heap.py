class MaxHeap:
    def __init__(self):
        self.heap=[]
    
    def parent(self,i):
        return (i-1)//2
    
    def leftchild(self,i):
        return 2*i+1
    
    def rightchild(self,i):
        return 2*i+2
    
    def print(self,arr=None):
        if not arr:
            print("Heap: "," - ".join([str(v) for v in self.heap]))
        else:
            print("Heap: "," - ".join([str(v) for v in arr]))
    
    def heapify_up(self,idx):
        if not self.heap:
            return None
        if len(self.heap)<idx:
            return None
        while idx>0 and self.heap[self.parent(idx)]<self.heap[idx]:
            self.heap[self.parent(idx)],self.heap[idx]=self.heap[idx],self.heap[self.parent(idx)]
            idx=self.parent(idx)
            
    def heapify_down(self,idx,size=None):
        if not size:
            size=len(self.heap)
        if not self.heap:
            return None
        if idx>=size:
            return None
        if idx<0:
            return None
        big=idx
        left=self.leftchild(idx)
        right=self.rightchild(idx)
        
        if left<size and self.heap[left]>self.heap[big]:
            big=left
        if right<size and self.heap[right]>self.heap[big]:
            big=right
        if big!=idx:
            self.heap[big],self.heap[idx]=self.heap[idx],self.heap[big]
            self.heapify_down(big,size=size)
            
    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
        
    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop() #pop last to first
        self.heapify_down(0) #heapify
        return root
               
    def build_heap(self,arr):
        self.heap=arr
        parent_idx=self.parent(len(self.heap)-1)
        for i in range(parent_idx,-1,-1):
            self.heapify_down(i)
    
    def sort_heap(self):
        for i in range(len(self.heap)-1,0,-1):
            self.heap[i],self.heap[0]=self.heap[0],self.heap[i]
            self.heapify_down(0,size=i)

            
if __name__=="__main__":
    heap=MaxHeap()
    heap.insert(4)
    heap.insert(5)
    heap.insert(2)
    heap.insert(10)
    heap.print()
    print("Extracted:",heap.extract_max())
    heap.print()
    unsrt_arr=[7,2,9,0,1,3]
    heap2=MaxHeap()
    heap2.build_heap(unsrt_arr)
    heap2.print()
    heap2.sort_heap()
    heap2.print()