""" 
Unit tests for the calculator library 
""" 
 
import os, sys 
 
# Add project root to Python path 
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")) 
sys.path.insert(0, project_root) 
 
from src.utils import add, sub, mul, div, exponent
 
class TestCalculator: 
 
    def test_addition(self): 
        assert 4 == add(2, 2) 
 

    def test_subtraction(self): 
        assert 2 == sub(4, 2)


    def test_multiplication(self):
        assert 6 == mul(3, 2)


    def test_division(self):
        assert 6 == div(12, 2)

    def test_exponent(self):
        assert exponent(2, 3) == 8