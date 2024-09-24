def find_password(n):
    result = ""
    used_pairs = set()  # множество для хранения уже использованных пар

    for i in range(1, n):  # первое число в паре
        for j in range(i + 1, n):  # второе число в паре
            if (i, j) not in used_pairs and (j, i) not in used_pairs:  # исключаем повторные пары
                if n % (i + j) == 0:  # проверяем кратность
                    result += str(i) + str(j)  # добавляем пару к результату
                    used_pairs.add((i, j))  # добавляем пару в использованные

    return result

# Пример использования:
print("Введите число для подбора пароля (от 3 до 20):")
n = input()

# Проверяем, что пользователь ввёл число, и что оно находится в диапазоне от 3 до 20
if n.isdigit():
    n = int(n)
    if 3 <= n <= 20:
        password = find_password(n)
        print(f"Пароль для числа {n}: {password}")
    else:
        print("Ошибка: Введите число в диапазоне от 3 до 20.")
else:
    print("Ошибка: Введите корректное число.")