import math

while True:
    choose = (input("Выберите действие: \n1. Сложение. \n2. Вычитание. \n3. Умножение. \n4. Деление. \n5. Степень. \n6. Квадратный корень. \n7. Факториал. \n8. Синус. \n9. Косинус. \n10. Тангенс. \n0. Выход. \n"))
    
    if choose == '0':
        break
    
    if choose not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        print("Ошибка, введите числа от 0 до 10")
        continue

    choose = int(choose)

    if choose == 1:
        a = int(input("Первое число: "))
        b = int(input("Второе число: "))
        print(a + b)
    if choose == 2:
        a = int(input("Первое число: "))
        b = int(input("Второе число: "))
        print(a - b)
    if choose == 3:
        a = int(input("Первое число: "))
        b = int(input("Второе число: "))
        print(a * b)
    if choose == 4:
        a = int(input("Первое число: "))
        b = int(input("Второе число: "))
        if b == 0:
            print("Делить на ноль нельзя")
        elif b != 0:
            print(a / b)
    if choose == 5:
        a = int(input("Число: "))
        b = int(input("Степень: "))
        print(a ** b)
    if choose == 6:
        a = int(input("Число "))
        if a < 0:
            print("Нельзя извлекать квадратный корень из отрицательного числа.")
        elif a >= 0:
            print(math.sqrt(a))
    if choose == 7:
        a = int(input("Число "))
        if a < 0:
            print("Нельзя вычислить факториал отрицательного числа.")
        elif a >= 0:
            print(math.factorial(a))
    if choose == 8:
        a = int(input("Градус: "))
        print(math.sin(a))
    if choose == 9:
        a = int(input("Градус: "))
        print(math.cos(a))
    if choose == 10:
        a = int(input("Градус: "))
        print(math.tan(a))