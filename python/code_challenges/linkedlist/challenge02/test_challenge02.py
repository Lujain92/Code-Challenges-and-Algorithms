from challenge02 import Node,Linked_list

def test_one():
    l=Linked_list()
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    l.push(5)
    assert l.middle()==[3,4,5]
def test_two():
    l=Linked_list()
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    l.push(5)
    l.push(6)
    assert l.middle()==[4,5,6]
