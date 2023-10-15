from bank import value

def test_hello():
    assert value('Hello') == 0

def test_hi():
    assert value('hi,how are you') == 20

def test_w():
    assert value("who's that")== 100