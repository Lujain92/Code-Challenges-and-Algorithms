# Write your test here
from .challenge02 import repeated

def test01():
    s="ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    expected= repeated(s)
    actual="ASAC"
    assert expected==actual
    
def test02():
    s="I am learning programming at ASAC."
    expected= repeated(s)
    actual="No Repetition"
    assert expected==actual

def test03():
    s="aa bb cc bb aa. dd"
    expected= repeated(s)
    actual="aa"
    assert expected==actual
