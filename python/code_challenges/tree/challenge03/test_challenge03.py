from challenge03 import BST,Tree

def test_one():
    T1=Tree()
    T1.root=BST([-10,-3,0,5,9])
    assert T1.BFS()==[0,-3,9,-10,5]



def test_two():
    T1=Tree()
    T1.root=BST([0,1,2,3,4,5])
    assert T1.BFS()==[3, 1, 5, 0, 2, 4]

def test_three():
    T1=Tree()
    T1.root=BST([1,3])
    assert T1.BFS()== [3,1] 