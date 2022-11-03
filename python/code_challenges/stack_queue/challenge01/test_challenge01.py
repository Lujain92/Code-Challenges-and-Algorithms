from challenge01 import MyQueue
import pytest

def test_one(fixed):
    
    assert fixed.pop()==1

def test_two(fixed):
    
    fixed.pop()
    fixed.pop()
    fixed.pop()
    assert fixed.empty()==True

def test_three(fixed):
    
    fixed.pop()
    fixed.pop()
    
    assert fixed.empty()==False

def test_four(fixed):
    
    assert  fixed.peek()==1


@pytest.fixture
def fixed():
    myQueue=MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    myQueue.push(3)
    return myQueue

