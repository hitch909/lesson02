# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

n = int(input("введите верхний предел таблици N=  "))
result = 0
for i in range(n+1):
    result = i ** 2
    print(result)
