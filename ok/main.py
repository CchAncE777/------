import unittest
from testing import TestFormula
from formula import Math_Y

if __name__ == '__main__':

    math = Math_Y(1, 2, 3)
    print(f'Правильное деление: {math.check_delit()}')
    print(f'Правильный логарифм: {math.check_log()}')
    print(f'Правильный ответ: {math.check_y()}')

    try:
        math_1 = Math_Y(1, 2, 1)
        math_1.check_delit()
    except ZeroDivisionError as e:
        print(f'Пожалуйста, введите число не равное 1(c). {e}')

    try:
        math_2 = Math_Y(0, 2, 3)
        math_2.check_log()
    except ValueError as e:
        print(f'Пожалуйста, введите число больше 0(a). {e}')

    try:
        math_3 = Math_Y('5v5y4fe4', 2, 1)
    except TypeError as e:
        print(f'Пожалуйста, введите вещественные числа. {e}')

    unittest.main()