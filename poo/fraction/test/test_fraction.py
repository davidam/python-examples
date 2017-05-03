import unittest
from app.fraction import Fraction

def test_default_fraction_gcd():
    f = Fraction(4, 4)
    assert f.gcd(4, 4) == 4

def test_default_fraction_reduce():
    f = Fraction(4, 4)
    assert f.reduce(5, 5) == (1, 1)


    

