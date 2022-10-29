# Write your test here
import pytest
from challenge03 import Linked_list
def test_one():
    l=Linked_list()
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    l.push(5)
    l.removeNthFromEnd(2)
    assert l.all_in_list()==[1,2,3,5]

    

def test_two():
    l=Linked_list()
    l.push(1)
    l.push(2)
    l.removeNthFromEnd(1)
    assert l.all_in_list()==[1]


def test_three():
    l=Linked_list()
    l.push(1)
    l.removeNthFromEnd(1)
    assert l.all_in_list()==[]


