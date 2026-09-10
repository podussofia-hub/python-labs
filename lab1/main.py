def obchyslyty_x(a, b):
    if a > b:
        return 2 * a + b
    elif a == b:
        return -2
    else:
        return (a - 5) / b


def pobuduvaty_piramidu(n):
    shyryna = len(" ".join([str(n)] * n))

    for chyslo in range(1, n + 1):
        ryadok = " ".join([str(chyslo)] * chyslo)
        print(ryadok.center(shyryna))

    for chyslo in range(n - 1, 0, -1):
        ryadok = " ".join([str(chyslo)] * chyslo)
        print(ryadok.center(shyryna))


print("ЗАВДАННЯ 1.")
print()

print("1. Обчислення значення X")

while True:
    try:
        a = float(input("Введіть значення a: ").replace(",", "."))
        b = float(input("Введіть значення b: ").replace(",", "."))

        if a < b and b == 0:
            print("Помилка: ділити на нуль не можна.")
            print("Спробуйте ще раз.\n")
            continue

        break

    except ValueError:
        print("Помилка: потрібно вводити тільки числа.")
        print("Спробуйте ще раз.\n")


x = obchyslyty_x(a, b)

print(f"Результат: X = {x}")

print()
print("2. Побудова піраміди")

while True:
    try:
        n = int(input("Введіть ціле число N від 1 до 10: "))

        if 1 <= n <= 10:
            break
        else:
            print("Помилка: N повинно бути від 1 до 10.")

    except ValueError:
        print("Помилка: потрібно ввести ціле число.")


print()
print("Отримана піраміда:")
pobuduvaty_piramidu(n)
