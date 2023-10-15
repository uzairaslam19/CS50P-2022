from twttr import shorten
def test_shorten():
    assert shorten('Twitter') =='Twttr'
def test_shorten2():
    assert shorten('Alphabet')=='lphbt'
def test_numeric():
    assert shorten('123')=='123'

def test_punt():
    assert shorten('twi,ter')=='tw,tr'