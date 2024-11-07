
from rpn_calc import RPN_Calc

import pytest

class TestRpnCalc:
    @pytest.fixture
    def rpn_calc(self):
        ''' Test fixture for class'''
        return RPN_Calc()
    @pytest.fixture
    def valid_test(self):
        nums = [5,4]
        ops = ['+', '-', '*', '/']
        answer = 9
        return nums, ops, answer
    # @pytest.fixture
    
    def test_rpn_is_class(self, rpn_calc):
        '''Tests the class can be instantiated'''
        assert rpn_calc is not None

    def test_calc_match_fail(self, rpn_calc):
        with pytest.raises(ValueError) as exc_info:
            ans = rpn_calc.calculate(5,4,'&')
        assert exc_info.value.args[0] == "Only operators accepted"

    def test_calc_add(self, rpn_calc, valid_test):
        '''Test add'''
        args = valid_test[0]
        op = valid_test[1][0]
        answer = valid_test[2]
        output = rpn_calc.calculate(args[0], args[1], op)
        assert output == answer

    def test_calc_subtract(self, rpn_calc, valid_test):
        '''Test Subtract'''
        args = valid_test[0]
        op = valid_test[1][1]
        t_ans = args[1] - args[0]
        result = rpn_calc.calculate(args[1], args[0], op)
        assert result == t_ans

    def test_calc_multiply(self, rpn_calc, valid_test):
        '''Test multiply'''
        args = valid_test[0]
        op = valid_test[1][2]
        t_ans = args[0] * args[1]
        result = rpn_calc.calculate(args[0], args[1], op)
        assert result == t_ans

    def test_calc_divide(self, rpn_calc):
        '''Test Divide'''
        args = 10, 5
        op = '/'
        t_ans = 2
        result = rpn_calc.calculate(args[0], args[1], op)
        assert t_ans==result

    def test_calc_div_zero(self, rpn_calc):
        with pytest.raises(ZeroDivisionError) as exc_info:
            ans = rpn_calc.calculate(5, 0, '/')
        assert exc_info.value.args[0] == "Cannot divide by zero"

    # def test_calc_expon(self):
    #     assert 1==1

