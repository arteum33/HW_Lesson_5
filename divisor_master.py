# Задание №1
# Функция проверки числа на простоту (простые числа - это те числа у которых делителиединица и они сами)

def divisor(n):
    x = len([i for i in range(1,n+1) if not n % i])
    # print(x)
    if x == 2:
        print('Простое число')
        return x
    else:
        # return x
        print('Число не относится к простым числам!')
        return x



# Задание №2
# Фукнция выводит список всех делителей числа

def divisors_list(a):
    list_1 = []
    for i in range(1, a + 1):
        if (a % i == 0):
            list_1.append(i)

    print(list_1)
    return list_1


# Задание №3
# Функция вывода самого большого простого делителя числа

def divisors_max_value(b):
    list_2 = []
    for i in range(1, b + 1):
        if (b % i == 0):
            list_2.append(i)
            list_3 = sorted(list_2,reverse=True)

    print(list_3[0])
    return list_3[0]




