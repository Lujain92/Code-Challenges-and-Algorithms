from challenge01 import create_tree

def test_one():
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    assert create_tree(preorder, inorder).value==3


def test_two():
   preorder=[-1]
   inorder=[-1]
   
   assert  create_tree(preorder, inorder).value == -1