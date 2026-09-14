def vydalyty_neparni(spysok):
    rezultat = []

    for i in range(len(spysok)):
        if (i + 1) % 2 == 0:
            rezultat.append(spysok[i])

    return rezultat


print("ЗАВДАННЯ 2.")

while True:
    try:
        vvedennya = input("Введіть цілі числа через пробіл: ").split()

        if len(vvedennya) == 0:
            print("Помилка: список не може бути порожнім.")
            continue

        spysok = [int(chyslo) for chyslo in vvedennya]
        break

    except ValueError:
        print("Помилка: потрібно вводити тільки цілі числа.")


print("Початковий список:")
print(spysok)

novyi_spysok = vydalyty_neparni(spysok)

print("Список після видалення елементів з непарними порядковими номерами:")
print(novyi_spysok)