class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BT:
    def __init__(self):
        self.root=None   #To initialize
    
    # inorder left,root,right
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=" > ")
        self.inorder(node.right)

    # preorder root,left,right
    def preorder(self,node):
        if node is None:  
            return
        print(node.data, end=" > ")
        self.preorder(node.left)
        self.preorder(node.right)
    
    # postorder left, right , root
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data,end=" > ")

    # level order traversal : todo
    # tree height : todo
    # tree constructor based on given data and selected traversal
    
if __name__=="__main__":
    bt=BT()
    bt.root=Node(0)
    bt.root.left=Node(1)
    bt.root.right=Node(2)
    bt.root.left.left=Node(3)
    bt.root.left.right=Node(4)
    bt.root.right.left=Node(5)
    bt.root.right.right=Node(6)

    bt.inorder(bt.root)
    print()
    bt.preorder(bt.root)
    print()
    bt.postorder(bt.root)
    print()