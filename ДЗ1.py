"""

1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько
чисел и строк и сохраните в переменные, выведите на экран.

"""

# name = input('Введите Ваше имя: ')
# age = int (input('Введите Ваш возраст: '))
# print('Привет, %s' % name + '!')
# print('Тебе уже %d лет! Ты в самом расцвете сил!' % age)

"""



2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и 
выведите в формате чч:мм:сс. Используйте форматирование строк.

"""
# t = int(input('Введите время в секундах: '))
# h = t // 3600
# m = t % 3600 // 60
# s = t % 3600 % 60
# print(f'{h:02d}:{m:02d}:{s:02d}')



"""

3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, 
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

"""
# n = input('Введите число: ')
# nn = n + n
# nnn = n + n + n
# otv = int(n) + int(nn) + int(nnn)
# print(otv)



"""

4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.

"""
# a = input('Введите целое положительно число: ')
# number_length = len(a)
# max = 0
# i = 0
# while i < number_length:
#     cur_el = int(a[i])
#     if cur_el > max:
#         max = cur_el
#     i += 1
# print(max)



"""

5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым 
результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность 
выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите 
прибыль фирмы в расчете на одного сотрудника.

"""
# v = int(input('Укажите значение выручки: '))
# i = int(input('Укажите значение издержек: '))
# r = (v - i) / v * 100
#
# if v < i:
#     print('Ваша фирма работает в убыток!')
#
# elif i < v:
#     print('Ваша фирма приносит доход!')
#     print('Ваша рентабельность составляет: ' + str(r) + '%')
#     s = int(input('Укажите число сотрудников: '))
#     ns = (v - i) / s
#     print('На каждого сотрудника приходиться по: ' + str(ns) + ' рублей')



"""

6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

"""
a = int(input('Результат спортсмена в первый день: '))
b = int(input('Желаемая дистанция: '))
days = 1
while a < b:
    a += 1.1
    days += 1

print(f'Спортсмен достигнет дистанции в {b} км за {days} дней')