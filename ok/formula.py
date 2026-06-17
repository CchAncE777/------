import math

class Math_Y():
    def __init__(self, a, b, c):
        if not all(isinstance(x, (int, float)) for x in (a, b, c)):
            raise TypeError('Прошу, введите все вещественные числа(пример: 3.12, 123412)')

        self._a = a
        self._b = b
        self._c = c

# Если ввести a, b, c в качестве строки и т.д., то у нас вылетит ошибка
# Типы данных кроме int и float не подходят для подсчета нашей формулы => учитываем этот случай


    def check_log(self):
        if self._a <= 0:
            raise ValueError('Пожалуйста, введите число, большее 0')
        
        self.log_a = math.log(self._a, 2)
        return self.log_a

# Мы берем число self._a в логарифм с основанием 2. Число может быть отрицательным, что будет для log являться ошибок.
# При self._a в логариф входит отрицательное число => ошибка вылезает ошибка. Для этого предусматриваем этот случай.

    def check_delit(self):
        if self._c == 1:
            raise ZeroDivisionError('Пожалуйста, введите число не равное 1')
        
        self.delit = self._b/(self._c - 1)
        return self.delit

# Все срабатывает при любых числах, не считая 1, так как в знаменателе у нас 0.
# При self._с = 1 в знаменателе вылезает 0 => ошибка. Предусматриваем этот случай через.

    def check_y(self):
        self.check_log()
        self.check_delit()

        y = self.log_a + self.delit
        return(y)
    
