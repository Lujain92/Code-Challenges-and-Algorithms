from challenge02 import isValid

def test_one():
    assert isValid("()")==True
def test_two():
    assert isValid("()[]{}")==True
def test_three():
    assert isValid("[({}]")==False
def test_four():
    assert isValid("[({hello})]")==True
def test_five():
    assert isValid("[(hello)()]")==True
def test_six():
    assert isValid("[{(())}]")==True
