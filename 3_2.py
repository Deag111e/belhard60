#Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3

#Решение:
number1 = input('Введите 1-ое число:')
number2 = input('Введите 2-ое число:')
number3 = input('Введите 3-е число:')

arifm_srednee = (float(number1) + float(number2) +float (number3))/3

print('Арифметическое среднее 3-ех чисел =',round(arifm_srednee,3))
