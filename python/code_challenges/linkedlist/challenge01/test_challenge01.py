from challenge01 import Node,Linked_list,delete


def test_push():
    link=Linked_list()
    node1=Node(4)
    node2=Node(5)
    link.push(node1)
    link.push(node2)
    

    assert link.all_in_list()==[4,5]

def test_delete():
    link=Linked_list()
    node1=Node(4)
    node2=Node(5)
    node3=Node(1)
    node4=Node(9)
    link.push(node1)
    link.push(node2)
    link.push(node3)
    link.push(node4)
    delete(node2)
    assert link.all_in_list()==[4,1,9]
    
def test_delete():
    link=Linked_list()
    node1=Node(4)
    node2=Node(5)
    node3=Node(1)
    node4=Node(9)
    link.push(node1)
    link.push(node2)
    link.push(node3)
    link.push(node4)
    delete(node3)
    assert link.all_in_list()==[4,5,9]