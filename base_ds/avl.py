class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class AVL:
    def __init__(self):
        self.root=None   
    
    def left_height(self,root):
        if not root:
            return 0
        left=self.left_height(root.left)
        return left+1
    
    def right_height(self,root):
        if not root:
            return 0
        right=self.right_height(root.right)
        return right+1
    
    def get_balance(self,root):
        lh=self.left_height(root)
        rh=self.right_height(root)
        # print(f"left height: {lh} | right height: {rh}")
        
        balance_factor=rh-lh
        return balance_factor
        # legal=[-1,0,1]
        
        # if balance_factor in legal:
        #     print("Balanced")
        #     return True
        # else:
        #     print("Unbalanced")
        #     return False
    
    def right_rotate(self,node):
        """"LL case"""
        left=node.left
        leftright=left.right
        
        #rotation
        node.left=leftright
        left.right=left
        
        return left
        
        
    def left_rotate(self,node):
        """RR Case"""
        right=node.right
        rightleft=right.left
        
        node.right=rightleft
        right.left=right
        
        return right
    
    def insert(self,root,value):
        if not root:
            node=Node(value)
            root=node
            print(f"{value} inserted to AVL")
            return root
        if value>root.value:
            root.right=self.insert(root.right,value)
        if value<root.value:
            root.left=self.insert(root.left,value)
            
        bf=self.get_balance(root) #balance factor
        
        ## bf > 1 , left size is more. bf < -1, right size is more
        
        # LL case
        if bf>1 and value < root.left.value: # if value was to be inserted in left - left
            return self.right_rotate(root)
        # LR case
        if bf>1 and value > root.left.value: # if value was to be inserted in left - right
            node.left=self.left_rotate(root.left)
            return self.right_rotate(root)
        # RR case
        if bf<-1 and value > root.right.value: # if value was to be inserted in right - right
            return self.left_rotate(root)
        # RL case
        if bf<-1 and value < root.right.value: # if value was to be inserted in right - left
            node.right=self.right_rotate(node.right)
            return self.left_rotate(root)
            
        
        return root
    
    def traverse(self,root):
        if not root:
            return
        self.traverse(root.left)
        print(root.value,end=" - ")
        self.traverse(root.right)


if __name__=="__main__":
    avl=AVL()
    avl.root=Node(6)
    avl.insert(avl.root,2)
    avl.insert(avl.root,8)
    avl.insert(avl.root,5)
    avl.insert(avl.root,10)
    avl.insert(avl.root,12)
    avl.traverse(avl.root)
    print()
    # avl.isbalance(avl.root)