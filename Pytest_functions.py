'''
Тест с использованием Pytest
Проверка функции вывода списка всех делителей числа
'''

from divisor_master import divisors_list
def test4_divisors_list():
    assert divisors_list(9) == [1, 3, 9]

'''
Тестирование функции нахождения максимального делителя числа
'''
from divisor_master import divisors_max_value
def test5_divisors_max_value():
    assert divisors_max_value(23648) == 23648

'''
Тестирование функции опеределения простого числа
'''

from divisor_master import divisor
def test6_divisor():
    assert divisor(3645) == 14 #у числа 3645 имеется 14с делителей и оно не является простым
    assert divisor(997) == 2


