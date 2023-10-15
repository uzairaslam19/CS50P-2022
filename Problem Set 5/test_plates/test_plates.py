from plates import is_valid

def test_minmax():
    assert is_valid('CS') == True
    assert is_valid('c') == False
    assert is_valid('AASDS') == True
    assert is_valid('AAAAAAA') ==False
    assert is_valid('12')==False

def test_number_placemnet():
    assert is_valid('AAA222')== True
    assert is_valid('AAA22A') == False
    assert is_valid('a23aa')== False

def test_zero_placement():
    assert is_valid('CS50')== True
    assert is_valid('CS05')==False

def test_punctuations():
    assert is_valid('PI.65') ==False
    assert is_valid('PS 12') == False
