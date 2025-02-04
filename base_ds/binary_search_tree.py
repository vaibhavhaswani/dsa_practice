## BST Operations

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    
    def traverse(self,node):
        #inorder for sort
        if node:
            self.traverse(node.left)
            print(node.data,end=" - ")
            self.traverse(node.right)
    
    def insert(self,root,data):
        if root is None:
            root=Node(data)
            print("Node Created!")
            return root

        if data<root.data:
            root.left=self.insert(root.left,data)
        else:
            root.right=self.insert(root.right,data)
        
        return root
    
    def search(self,root,key):
        if root is None or root.data==key:
            return root
        if key<root.data:
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)
        
    def find_min(self):
        if self.root is None:
            print("Tree is Empty!")
            return None
        root=self.root
        while root.left:
            root=root.left
        print(f"Minimum node: {root.data}")
        return root.data
    
    def find_max(self):
        if self.root is None:
            print("Tree is Empty")
            return None
        root=self.root
        while root.right:
            root=root.right
        print(f'Maximum node: {root.data}')
        return root.data
    
    def get_height(self,root):
        if root is None:
            return 0
        left,right=self.get_height(root.left),self.get_height(root.right)
        return max(left,right)+1
    
    def delete(self,root,key):
        # case 1 : node is leaf node , assign null
        # case 2 : node has single child, replace with child and assign null to child
        # case 3 : node has both child, replace with inorder successor or predcessor (smallest element in right subtree or biggest element in left sub tree) and assign none when at leaf
        if root.data>key:
            # if key value is lesser than root calling delete in left sub tree to find and delete value
            root.left = self.delete(root.left,key)
        elif root.data<key:
            # if key value is greater than root calling delete in right sub tree to find and delete value
            root.right = self.delete(root.right,key)
        else:
            #if key is found
            if root.left is None:
                #if the found root has no left subtree right subtree node will be returned to assigned as root 
                return root.right
            if root.right is None:
                # if the found root has no right subtree left subtree node will be returned to assigned as root 
                return root.left
            #if it has both child
            # find the inorder succecor or the minimum in right sub tree
            curr=root.right
            while curr.left:
                curr=curr.left
            # replace the value of root with minimum value in right sub tree
            root.data = curr.data
            # recursively delete that repeating cursor value, from the right tree
            root.right = self.delete(root.right,curr.data)
        return root
        
    def lca(self,root,n1,n2):
    # lowest common ancestor is the closest node ancestor to the two nodes given
        if root is None:
            #if tree is empty
            return None
        if root.data > n1 and root.data > n2: #if root key is greater then lca should be in left sub tree
            return self.lca(root.left,n1,n2)
        elif root.data < n1 and root.data > n2: #if root key is lower then lca should be in right sub tree
            return self.lca(root.right,n1,n2)
        return root # if both are not greater or lesser then root is the lca
     
    def from_array(self,arr):
        #create BST from a sorted array
        if not arr:
            return None
        ifsort=all([arr[i]<arr[i+1] for i in range(len(arr)-1)])
        if not ifsort:
            return None
        mid=len(arr)//2
        node=Node(arr[mid])
        node.left=self.from_array(arr[:mid])
        node.right=self.from_array(arr[mid+1:])
        return node
        
         

if __name__=="__main__":
    bst=BST()
    bst.root=bst.insert(bst.root,4)
    bst.root=bst.insert(bst.root,5)
    bst.root=bst.insert(bst.root,1)
    bst.root=bst.insert(bst.root,9)
    bst.root=bst.insert(bst.root,3)
    bst.find_min()
    bst.find_max()
    print("Tree Height:",bst.get_height(bst.root))
    bst.traverse(bst.root)
    print()
    tempnode=bst.search(bst.root,5)
    print(f"Node {tempnode.data}'s left : {tempnode.left} | right : {tempnode.right.data}")
    bst.root=bst.insert(bst.root,2)
    bst.root=bst.insert(bst.root,0)
    bst.root=bst.insert(bst.root,6)
    bst.root=bst.insert(bst.root,7)
    bst.traverse(bst.root)
    print()
    #bst now
    #      4
    #     / \
    #     1   5
    #     / \   \
    #     0   3   9
    #         /   /
    #         2   7
    #         6
    n1,n2=6,7
    print(f"LCA of node {n1} and {n2} is {bst.lca(bst.root,n1,n2).data}")
    key=1
    print(f'Deleting {key} from tree')
    del_bst=bst.delete(bst.root,key)
    bst.traverse(del_bst)
    print()
    arr=[1,2,3,4,5,6,7,8,9]
    print(f"Creating Tree from {arr}")
    arr_root=bst.from_array(arr)
    arr_bst=BST()
    arr_bst.root=arr_root
    arr_bst.traverse(arr_root)
    print()
    tempnode=arr_bst.search(arr_bst.root,5)
    print(f"Node {tempnode.data}'s left : {tempnode.left.data} | right : {tempnode.right.data}")
    
    