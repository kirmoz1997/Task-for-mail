import pytest
def test_strings_a_3():
    assert "a" * 3 == "aaa"


def test_In_Symbol():
    assert "h" in "hello"

def testIsStr():
    res = "test"
    assert isinstance(res,str)


def testIntersection():
    setA = set("135")
    setB = set("168")
    setC = set("1");
    assert setA.intersection(setB) == setC

def testUnion():
    setA = set("123")
    setB = set("456")
    setC = set("123456")
    assert setA.union(setB) == setC

def testDiff():
    setA = set("123")
    setB = set("234")
    setC = set("1")
    assert setA.difference(setB) == setC

def testNegative():
    setA = set([1,2,3])
    value = [0,1,2]
    temp = ""
    i = 0

    for val in setA:
        try:
            temp += str(val/value[i])+";"
        except ZeroDivisionError:
            pass
        i+=1
    assert temp == "2.0;1.5;"



testA = "3"
testB = "3"
@pytest.mark.parametrize("a", testA)
@pytest.mark.parametrize("b",testB)
def testParam(a,b):
    assert a == b


