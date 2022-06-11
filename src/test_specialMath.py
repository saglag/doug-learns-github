from specialMath import add, multiply


def test_add():
    assert add(1,4) == 5
def test_multiply():
    assert multiply(2,2) == 4
    assert multiply(5,10) == 50
    assert multiply(12,12) == 144
    assert multiply(0,0) == 0
    assert multiply(1,0) == 0
    assert multiply(0,1) == 0
    assert multiply(0,-1) == 0
    assert multiply(0, 0.5) == 0
    assert multiply(-1,2) == -2
    