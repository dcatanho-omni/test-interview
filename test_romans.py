import pytest
from romans import to_roman

def test_one():
    output = to_roman(1)
    assert output == 'I'

#def test_ten():

