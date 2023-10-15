from numb3rs import validate

def test_correct():
    assert validate('1.2.3.4') == True
    assert validate('192.168.7.21') == True
    assert validate('0.0.0.0') == True
    assert validate('255.255.255.255') == True

def test_incorrect():
    assert validate('275.12.43.44') == False
    assert validate('cat') == False
    assert validate('255.277.277.277') == False