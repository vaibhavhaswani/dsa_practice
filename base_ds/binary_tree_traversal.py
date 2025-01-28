from collections import deque


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
    
    # breadh first search \ level order
    def levelorder(self,node):
        if node is None:
            print("Tree is Empty!")
            return 
        queue=deque([node])  # 0
        while queue:
            current=queue.popleft()           # 0 popped 1 popped
            print(current.data,end=" > ")
            
            if current.left:
                queue.append(current.left)   # [1] [2,3]
            if current.right:
                queue.append(current.right)  # [1,2] [2,3,4]

        # breadh first search \ level order without queue
    def levelorder(self,node):
        if node is None:
            print("Tree is Empty!")
            return 
        queue=[node] # 0
        while queue:
            current=queue.pop(0)           # 0 popped 1 popped
            print(current.data,end=" > ")
            
            if current.left:
                queue.append(current.left)   # [1] [2,3]
            if current.right:
                queue.append(current.right)  # [1,2] [2,3,4]
    
    def _getheight(self):
        if self.root is None:
            print("Tree is Empty!")
            return
        
        queue=deque([self.root])
        i=0
        left=[]
        right=[]
        while queue:
            current=queue.popleft()

            if current.left:
                left.append(current.left)
                queue.append(current.left)
            if current.right:
                right.append(current.right)
                queue.append(current.right)

            
        return max(len(left),len(right))
        
    # get tree height through recursion
    def getheight(self,node): #optimal
        if node is None:
            return 0
        left=self.getheight(node.left)
        right=self.getheight(node.right)
        
        return max(left,right)+1
    
    # tree constructor based on given data and selected traversal
    @classmethod
    def buildtree(self,traversal:dict):
        #if inorder and preorder list are given
        if 'inorder' in list(traversal.keys()) and 'preorder' in list(traversal.keys()):
            pre=traversal['preorder'] # preorder traversal , root in the beginning
            ino=traversal['inorder'] # inorder traversal has root in the middle of left and right

            if not pre or not ino:
                return None

            root_data=pre.pop(0)
            root=Node(root_data)

            root_index=ino.index(root_data)
            ino_left,ino_right=ino[:root_index],ino[root_index+1:]

            root.left=self.buildtree({"inorder":ino_left,"preorder":pre})
            root.right=self.buildtree({"inorder":ino_right,"preorder":pre})

            return root
        
        #if inorder and post order list are given
        elif 'inorder' in list(traversal.keys()) and 'postorder' in list(traversal.keys()):
            post=traversal['postorder'] # postorder traversal , root in the end
            ino=traversal['inorder'] # inorder traversal has root in the middle of left and right

            if not post or not ino:
                return None
            
            root_data=post.pop()
            root=Node(root_data)

            root_index=ino.index(root_data)

            ino_left,ino_right=ino[:root_index],ino[root_index+1:]

            # right tree will be built first as of post order (reverse)
            root.right=self.buildtree(traversal={"inorder":ino_right,"postorder":post})
            root.left=self.buildtree(traversal={"inorder":ino_left,"postorder":post})

            return root
        
        #if levelorder list is given
        elif 'levelorder' in list(traversal.keys()):
            lvl=traversal['levelorder']
            if not lvl or lvl[0] is None:
                return None
            root_data=lvl[0]
            root=Node(root_data)
            q=[root]
            i=1
            while i<len(lvl):
                current=q.pop(0)                           # node 1 , node1.left (similarly left and right nodes of node1.left will be created then node1.right)
                if i<len(lvl) or lvl[i] is not None:       
                    current.left=Node(lvl[i])               # node1.left = i[1]=2
                    q.append(current.left)                  # [node1.left]
                i+=1                                        # i=2
                if i<len(lvl) or lvl[i] is not None:
                    current.right=Node(lvl[i])             # node1.right = i[2] =3 
                    q.append(current.right)               # [node1.left,node1.right]
                i+=1                                     # i = 3
            return root


        return None

    
if __name__=="__main__":
    bt=BT()
    bt.root=Node(0)
    bt.root.left=Node(1)
    bt.root.right=Node(2)
    bt.root.left.left=Node(3)
    bt.root.left.right=Node(4)
    bt.root.right.left=Node(5)
    bt.root.right.right=Node(6)
    bt.root.right.right.left=Node(8)

    bt.inorder(bt.root)
    print()
    bt.preorder(bt.root)
    print()
    bt.postorder(bt.root)
    print()
    bt.levelorder(bt.root)
    print()
    print(f"Tree height: {bt._getheight()}")
    print(f"Tree height: {bt.getheight(bt.root)}")

    # tree_dict={"inorder":[4,2,5,1,6,3,7],"preorder":[1,2,4,5,3,6,7]}
    # tree_dict={"inorder":[4,2,5,1,6,3,7],"postorder":[4,5,2,6,7,3,1]}
    tree_dict={"levelorder":[1,2,3,4,5,6,7]}

    root=BT.buildtree(traversal=tree_dict)
    tree=BT()
    tree.root=root
    tree.preorder(tree.root)
    print()
    tree.levelorder(tree.root)
    print()