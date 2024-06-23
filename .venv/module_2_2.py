first = input('Первое число: ')
second = input('Второе число: ')
third = input('Третье число: ')
if first == second and second == third :  # наименее вероятное условие
    print(3)
elif first == second or first == third or second == third :  # наиболее вероятное условие
    print(2)
else:
    print(0)

