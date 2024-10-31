""" RPN_CALC: a RPN calculator
    By: James R. Brown
"""

class RPN_Calc:

    def __init__(self):
        self.nums = []
        self.ops = []


    def calculate(self, args = None):
        ''' calculates the answer '''

        self.__sep_args(args = args)

        answer = 0

        while len(self.ops) > 0:
            op = self.ops.pop()
            num2 = self.nums.pop()
            num1 = self.nums.pop()
            temp = 0

            match op:
                case '+':
                    temp = self.__add(num1, num2)
                case '-':
                    temp = self.__subtract(num1, num2)
                case '*':
                    temp = self.__multiply(num1, num2)
                case '/':
                    temp = self.__divide(num1, num2)
                case '^':
                    temp = self.__expo(num1, num2)
                case _:
                    temp = 0
                    # print('Not an operation')
                    raise ValueError("Only operators accepted")
            answer += temp

        return temp

    def __sep_args(self, args):
        '''Separates the numbers and the operator to lists from received argument'''
        if args is not None:
            for x in args:
                if x.isdigit():
                    self.nums.append(int(x))
                else:
                    self.ops.append(x)

    def __expo(self, a, b):
        return a**b

    def __add(self, a, b):
        return a + b;

    def __subtract(self, a, b):
        return a - b

    def __multiply(self, a, b):
        return a * b

    def __divide(self, a, b):
        if b != 0:
            return a // b