from challenge02 import isValid

def test_one():
    assert isValid("()")==True
def test_two():
    assert isValid("()[]{}")==True
def test_three():
    assert isValid("[({}]")==False

