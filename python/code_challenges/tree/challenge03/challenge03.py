
class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
class Tree:
    def __init__(self):
        self.queue=[]
        self.root=None
    def BFS(self):
        '''
        this method to print the values of nodes by Breadth First Search
        output:list
        '''
        tree=[]
        if not self.root:
            return 'Empty tree'
        node= self.root
        self.queue.append(node)
        while self.queue:
            node= self.queue.pop(0)
            tree.append(node.value)
            if node.left != None:
                self.queue.append(node.left)
            if node.right != None:
                self.queue.append(node.right)
        return tree

def BST( nums):
    """
    function BST used to convert list of inhger to high balanced BST
    :type nums: List[int]
    :rtype: TreeNode
    """
    mid= len(nums)//2
    if not nums:   
        return None
    return Node(nums[mid], BST(nums[:mid]), BST(nums[mid+1:]))



        