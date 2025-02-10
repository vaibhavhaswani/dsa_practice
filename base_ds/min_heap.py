## Min Heap is Binary Tree with smallest value always as root

class MinHeap:
    def __init__(self):
        self.heap=[]
        
    def parent(self,i):
        """gets the parent index of the node"""
        return (i-1)//2
    
    def leftchild(self,i):
        """returns the left child of the node"""
        return 2*i+1
    
    def rightchild(self,i):
        """returns the right child index of the node"""
        return 2*i+2
    
    def print(self,arr=None):
        if not arr:
            print("Heap: "," - ".join([str(v) for v in self.heap]))
        else:
            print("Heap: "," - ".join([str(v) for v in arr]))
    
    
    def heapify_up(self,index): #or bubble up
        """resets the heap, from given index, checks if index value is greater than parent as it's MinHeap else issue swap"""
        while index>0 and self.heap[index]<self.heap[self.parent(index)]:
            #keep swapping till current index is less than parent
            self.heap[index],self.heap[self.parent(index)]=self.heap[self.parent(index)],self.heap[index]
            #reset the current index\
            index=self.parent(index)
            
    def heapify_down(self,index):
        """Assume the current node (index) is the smallest.
            Find the left and right children using:

                left_child(i) = 2i + 1
                right_child(i) = 2i + 2

            Compare with children:

                If left child is smaller, update smallest = left_child.
                If right child is smaller than smallest, update smallest = right_child.

            If smallest is not the current node, swap and recurse to maintain the heap property."""
        smallest=index
        left=self.leftchild(index)
        right=self.rightchild(index)
        
        if left<len(self.heap) and self.heap[left]<self.heap[smallest]:
            smallest=left
        if right<len(self.heap) and self.heap[right]<self.heap[smallest]:
            smallest=right
        if smallest!=index:
            self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
            self.heapify_down(smallest) #smallest is the new index
            
    def insert(self,value):
        # Steps:
        # Add the new value at the end of the heap (in the last available position).
        # Check if the heap property is violated (i.e., if the new node is smaller than its parent).
        # If violated, swap it with the parent (move it upward) until the heap property is restored.
        # This process is called Heapify Up (or Bubble Up)
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1) #sending last index reset the heap if violate
            
    def extract_min(self):
        """The smallest element (root) is removed.
            The last element is moved to the root.
            heapify_down is called to restore the heap order."""
        # removes smallest item and returns it
        if not self.heap:
            return None
        if len(self.heap)==1:
            return self.heap.pop(0)
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0) # resets the heap
        
        return root
    
    def build_heap(self,arr):
        self.heap=arr[:]
        idx=self.parent(len(arr)-1)
        for i in range(idx,-1,-1):
            self.heapify_down(i)
        
        
if __name__=="__main__":
    heap=MinHeap()
    heap.insert(4)
    heap.insert(5)
    heap.insert(2)
    heap.insert(10)
    heap.print()
    print("Extracted:",heap.extract_min())
    heap.print()
    unsrt_arr=[7,2,9,0,1,3]
    heap2=MinHeap()
    heap2.build_heap(unsrt_arr)
    heap2.print()
    