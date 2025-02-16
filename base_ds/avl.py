class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.height = 1 #height of node

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
    
    def is_balance(self,root):
        lh=self.left_height(root)
        rh=self.right_height(root)
        # print(f"left height: {lh} | right height: {rh}")
        
        balance_factor=rh-lh
        # return balance_factor
        # legal=[-1,0,1]
        
        if balance_factor <=1 and balance_factor>=-1:
            print("Balanced")
            return True
        else:
            print("Unbalanced")
            return False
        
    def get_height(self,node):
        return node.height if node else 0
    
    def get_balance(self,node):
        return self.get_height(node.left)-self.get_height(node.right) if node else 0
    
    def right_rotate(self,node):
        """"LL case"""
        left=node.left
        leftright=left.right
        
        #rotation
        left.right=node
        node.left=leftright
        
        
        node.height=max(self.get_height(node.right),self.get_height(node.left))+1
        left.height= max(self.get_height(left.right),self.get_height(left.left))+1
        
        return left
        
        
    def left_rotate(self,node):
        """RR Case"""
        right=node.right
        rightleft=right.left
        
        right.left=node
        node.right=rightleft
        
        
        node.height = max(self.get_height(node.left),self.get_height(node.right))+1
        right.height= max(self.get_height(right.left),self.get_height(right.right))+1  
        
        return right
    
    def insert(self,root,value):
        if not root:
            root=Node(value)
            print(f"{value} inserted to AVL")
            return root
        if value>root.value:
            root.right=self.insert(root.right,value)
        if value<root.value:
            root.left=self.insert(root.left,value)
            
        root.height = max(self.get_height(root.left),self.get_height(root.right))+1
            
        bf=self.get_balance(root) #balance factor
        
        ## bf > 1 , left size is more. bf < -1, right size is more
        
        # LL case
        if bf>1 and value < root.left.value: # if value was to be inserted in left - left
            return self.right_rotate(root)
        # LR case
        if bf>1 and value > root.left.value: # if value was to be inserted in left - right
            root.left=self.left_rotate(root.left)
            return self.right_rotate(root)
        # RR case
        if bf<-1 and value > root.right.value: # if value was to be inserted in right - right
            return self.left_rotate(root)
        # RL case
        if bf<-1 and value < root.right.value: # if value was to be inserted in right - left
            root.right=self.right_rotate(root.right)
            return self.left_rotate(root)
            
        
        return root
    
    def delete(self,node,key):
        if not node:
            return None
        if key>node.value:
            node.right=self.delete(node.right,key)
        elif key<node.value:
            node.left=self.delete(node.left,key)
        else: # if value of node matches the key
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            temp=node
            temp=temp.right
            while temp.left:
                temp=temp.left
            node.value=temp.value
            node.right = self.delete(node.right,temp.value)
        
        #rebalance
        if not node.left and not node.right:
            return node
        node.height = max(self.get_height(node.left),self.get_height(node.right))+1
        
        bf = self.get_balance(node) # balance factor
        
        if bf>1: #Left dominant
            if self.get_balance(node.left)>=0: # LL
                return self.right_rotate(node) #return rotated root
            else: #LR case
                node.left=self.right_rotate(node.left)
                return self.left_rotate(node)
        if bf<-1: #right dominant
            if self.get_balance(node.right)<=0: #RR
                return self.left_rotate(node)
            else:
                node.right=self.left_rotate(node.right)
                return self.right_rotate(node)
            
        return node
            
    
    def traverse(self,root):
        if not root:
            return
        self.traverse(root.left)
        print(root.value,end=" - ")
        self.traverse(root.right)


if __name__=="__main__":
    avl=AVL()
    keys=[10, 20, 30, 40, 50, 25]
    for k in keys:
        avl.root=avl.insert(avl.root,k)
    avl.traverse(avl.root)
    print()
    avl.root=avl.delete(avl.root,20)
    avl.traverse(avl.root)
    print()
    # avl.isbalance(avl.root)