""" RPN_CALC: a RPN calculator
    By: James R. Brown
"""

class RPN_Calc:

    def __init__(self):
        self.answer = None

    # def rpn_calc(self, num1, num2, op):
    #     '''Parses the expression passed'''
    #     pass

    def calculate(self, num1, num2, op):
        ''' calculates the answer '''

        # self.__sep_args(args = args)

        temp = 0

        match op:
            case '+':
                temp = num1 + num2
            case '-':
                temp = num1 - num2
            case '*':
                temp = num1 * num2
            case '/':
                temp = self.__divide(num1, num2)
            case '^':
                temp = self.__expo(num1, num2)
            case _:
                # print('Not an operation')
                raise ValueError("Only operators accepted")

        return temp

    def __expo(self, a, b):
        return a**b

    def __divide(self, a, b):
        if b != 0:
            return a // b
        else:
            raise ZeroDivisionError()
