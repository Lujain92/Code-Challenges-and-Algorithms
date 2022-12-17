# Write your test here
from challenge02 import repeated

def test_01():
    s="ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    expected= repeated(s)
    actual="ASAC"
    assert expected==actual
    
def test_02():
    s="I am learning programming at ASAC."
    expected= repeated(s)
    actual="No Repetition"
    assert expected==actual

def test_03():
    s="aa bb cc bb aa. dd"
    expected= repeated(s)
    actual="aa"
    assert expected==actual
