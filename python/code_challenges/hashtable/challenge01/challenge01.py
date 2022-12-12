class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
class Tree:
    def __init__(self):
        self.root=None
    def insert(self,val):
        new_node=Node(val)
        if not self.root:
            self.root=new_node

        
        curr=self.root
        while True :
            if val==curr.value:
                return "Can't added"
            if curr.value > val:
                if  not curr.left:
                    
                    curr.left=new_node
                    return 
               
                curr=curr.left
                
            elif  curr.value < val :
                if  not curr.right:
                    curr.right=new_node
                    return
                
                curr=curr.right

    # def insert(self,val):
        
    #     if not self.root:
    #         self.root=Node(val)
    #         return self.root
    #     if val > self.root.val:
    #         self.root.right=self.insert(val)
            
    #     elif val < self.root.val:
    #         self.root.left=self.insert(val)
    #     return self.root
#Write here the code challenge solution
def findTarget(root, k) :
        '''
        function find target accept 2 argument and check 
        if the root has 2 node value equal to target 
        if yes return true otherwise false
        '''
        s=set()
        def dfs(root):
            if root:
                if root.value in s:
                    return True
                s.add(k-root.value)
                return dfs(root.left) or dfs(root.right)
            return False
        return dfs(root)

