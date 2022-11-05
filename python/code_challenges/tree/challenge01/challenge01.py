class Node:
    '''
    class node used to create node
    '''
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None



def create_tree(preorder, inorder):
    '''
    class create_tree used to create tree from preorder and inorder list
    input inorder,preorder:list,list
    output :tree
    '''
    if inorder:
        i = inorder.index(preorder.pop(0))
        root = Node(inorder[i])
        root.left = create_tree(preorder, inorder[0:i])
        root.right = create_tree(preorder, inorder[i+1:])
        return root
            