# Задание 1
var_int = 10
var_str = 'string1'

print(var_int)
print(var_str)

var_input_int = int(input())
var_input_str = input()

print(var_input_int)
print(var_input_str)

# Задание 2
seconds = int(input('Введите время в секундах: '))
hours = seconds//3600
minutes = (seconds-hours*3600)//60
seconds = seconds - hours*3600 - minutes*60
print(f'{hours}:{minutes}:{seconds}')

# Задание 3
number = input('Введите число: ')
number_2 = number+number
number_3 = number+number+number

number = int(number)
number_2 = int(number_2)
number_3 = int(number_3)
summ = number+number_2+number_3

# Задание 4
number = input('Введите целое положительное число: ')
number_list = []
count = len(number)

while(count > 0):
    number_list.append(int(number[count-1]))
    count -= 1

print(f'Максимальное число: {max(number_list)}')

# Задание 5
proceeds = int(input('Укажите выручку: '))
costs = int(input('Укажите издержки: '))

profit = proceeds-costs
profitabitily = 1.0

if profit > 0:
    print('Ваша компания прибыльна.')
    profitabitily = round(profit / costs, 2) * 100
    print(f'Рентабельность составляет {int(profitabitily)}%')
    number_of_employees = int(input('Введите количество сотрудников: '))
    profit_per_employee = round(profit / number_of_employees, 2)
    print(f'Прибыль на сотрудника {profit_per_employee}')
else:
    print('Ваша компания убыточна.')

# Задание 6
a = int(input('Введите a: '))
b = int(input('Введите b: '))
day = 1

while(a < b):
    print(f'{day}-й день: {a}')
    a = round(a + a * 0.1, 2)
    day += 1

print(f'{day}-й день: {a}')

print(f'Ответ: на {day}-й день спортсмен достиг результата - не менее {b} км.')
