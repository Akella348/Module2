def get_matrix(n,m,value):
    matrix = []  # вводим пустой список
    for i in range(n):  # вводим цикл для каждого числа в строке n
        matrix.append([])  # добавляем список, который ляжет внутрь списка вне цикла
        for j in range(m):  # вводим цикл, складывающий значение value в i-ый объект списка,т.е. строки
            matrix[i].append(value)
    return matrix  # возвращаем значение
result1 = get_matrix(2, 2, 10)  # присваеваем значение функции переменной
result2 = get_matrix(3, 5, 42)  # присваеваем значение функции переменной
result3 = get_matrix(4, 2, 13)  # присваеваем значение функции переменной
print(result1)
print(result2)
print(result3)
