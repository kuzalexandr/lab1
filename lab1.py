import sys

def biquadratic(a, b, c):

    # Вычисляем дискриминант
    discriminant = b**2 - 4*a*c

    roots = []  # Список для хранения корней

    # Проверяю дискриминант
    if discriminant >= 0:

        x2_1 = (-b + discriminant**0.5) / (2*a)
        x2_2 = (-b - discriminant**0.5) / (2*a)


        if x2_1 >= 0:
            roots.append(x2_1**0.5)
            roots.append(-x2_1**0.5)
        if x2_2 >= 0:
            roots.append(x2_2**0.5)
            roots.append(-x2_2**0.5)

    return roots

if name == "main":

    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
        except ValueError:
            print("Некорректные значения коэффициентов")
            sys.exit(1)
    else:
        # Вводим коэффициенты с клавиатуры
        while True:
            try:
                a = float(input("Введите коэффициент A: "))
                break
            except ValueError:
                print("Некорректное значение для коэффициента A")
        while True:
            try:
                b = float(input("Введите коэффициент B: "))
                break
            except ValueError:
                print("Некорректное значение для коэффициента B")
        while True:
            try:
                c = float(input("Введите коэффициент C: "))
                break
            except ValueError:
                print("Некорректное значение для коэффициента C")

    
    roots = biquadratic(a, b, c)

    # результат
    if roots:
        print("Действительные корни уравнения:")
        for root in roots:
            print(root)
    else:
        print("Уравнение не имеет действительных корней")
