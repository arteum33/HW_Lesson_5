from divisor_master import divisor,divisors_list, divisors_max_value

# Тест №1: Функция определения простого числа

if divisor(37) != 2: #у числа 37 - 2 делителя
    print ('Определение простого числа - Test-№1 Failed')
if divisor(884) != 12: #у числа 884 - 12 делителя
    print ('Определение простого числа - Test-№1 Failed')
print('Тест №1 успешно пройден')


# Тест №2: Фукнция выводит список всех делителей числа

if divisors_list (9) != [1, 3, 9]: #делители часла 9: 1, 3, 9
    print("Список делителей - Test-№2 Failed")
print('Тест №2 успешно пройден')



# Тест №3: Функция вывода самого большого простого делителя числа

if divisors_max_value (999) != 999: #максимальный делитель числа 999 = 999
    print("Максимальный делитель - Test-№3 Failed")
print('Тест №3 успешно пройден')