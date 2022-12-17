from challenge01 import findTarget, Tree,Node

r=Tree()
r.insert(5)
r.insert(3)
r.insert(6)
r.insert(2)
r.insert(4)
r.insert(7)


def test_one():
    assert findTarget(r.root,9)==True

def test_two():
    assert findTarget(r.root,8)==True

def test_three():
    assert findTarget(r.root,91)==False

def test_four():
    q=Tree()
    assert findTarget(q.root,91)==False
def test_four():
    q=Tree()
    assert findTarget(q.root,91)==False
def test_five():
    l=Tree()
    l.insert(1)
    assert findTarget(l.root,1)==False