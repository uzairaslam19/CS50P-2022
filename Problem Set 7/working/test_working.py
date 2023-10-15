from working import convert
import pytest
def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("5:00 AM to 5:00 PM")== "05:00 to 17:00"

def test_12am():
    assert convert("12 AM to 12 PM")=="00:00 to 12:00"
    assert convert("12:00 AM to 12:30 PM")=="00:00 to 12:30"

submit50 cs50/problems/2022/python/workingdef test_omit_to():
    with pytest.raises(ValueError):
        convert("3 PM  4 AM")
def test_outofrange():
    with pytest.raises(ValueError):
        convert("3:60 PM to 5:80 AM")