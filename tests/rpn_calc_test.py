
from rpn_calc import RPN_Calc

import pytest

class TestRpnCalc:
    @pytest.fixture
    def rpn_calc(self):
        ''' Test fixture for class'''
        return RPN_Calc()
    @pytest.fixture
    def valid_test(self):
        args = '54+'
        answer = 9
        return args, answer
    # @pytest.fixture
    
    def test_rpn_is_class(self, rpn_calc):
        '''Tests the class can be instantiated'''
        assert rpn_calc is not None

    def test_calc_match_fail(self, rpn_calc):
        with pytest.raises(ValueError) as exc_info:
            ans = rpn_calc.calculate('54&')
        assert exc_info.value.args[0] == "Only operators accepted"

    def test_calc_add(self):
        assert 1==1

    def test_calc_subtract(self):
        assert 1==1

    def test_calc_multiply(self):
        assert 1==1

    def test_calc_divide(self):
        assert 1==1

    def test_calc_div_zero(self):
        assert 1==1

    def test_calc_expon(self):
        assert 1==1

