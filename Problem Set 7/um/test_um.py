from um import count

def test_um_part_of_word():
    assert count("yummy") == 0
    assert count("Gum") == 0
    assert count("Yum") == 0

def test_um():
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1
    assert count("hello, um, world") == 1
    assert count("um, hello there, um, how are you?") == 2

def test_0um():
    assert count("The icecream is yummy") == 0
    assert count("The taste is yum") == 0

def test_caps_um():
    assert count("UM..") == 1