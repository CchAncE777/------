import math

class Math_Y():
    def __init__(self, a, b, c):
            self._a = a
            self._b = b
            self._c = c

    def check_log(self):
        if self._a <= 0:
            raise ValueError('Пожалуйста, введите число, большее 0')
        
        self.log_a = math.log(self._a, 2)
        return self.log_a

#При self._a в логариф входит отрицательное число => ошибка вылезает ошибка

    def check_delit(self):
        if self._c == 1:
            raise ZeroDivisionError('Пожалуйста, введите число не равное 1')
        
        self.delit = self._b/(self._c - 1)
        return self.delit
    
#При self._с = 1 в знаменателе вылезает 0 => ошибка 

    def check_y(self):
        self.check_log()
        self.check_delit()

        y = self.log_a + self.delit
        print(y)
    
try:
    a = float(input('Пожалуйста, введите число в логариф большее 0: ')),
    b = float(input('Пожалуйста, введите число в числитель: '))
    c = float(input('Пожалуйста, введите число в знаменатель не равное 1:'))

    M = Math_Y(a, b, c)
    M.check_y()

except ValueError:
    print('Ошибка. Введите числовые значения, а также не комплексные')
