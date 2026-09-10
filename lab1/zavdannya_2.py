from lab1.modul_vyraz import obchyslyty_y
from lab1.modul_riadok import stvoryty_riadok


def vvesty_x():
    while True:
        try:
            return float(input("Введіть значення x: ").replace(",", "."))
        except ValueError:
            print("Помилка: потрібно ввести число.")


while True:
    print()
    print("ЗАВДАННЯ 2.")
    print("1 - Обчислити y = sin²(x) + cos²(x)")
    print("2 - Вивести рядок із 20 символів")
    print("0 - Завершити програму")

    vybir = input("Оберіть дію: ")

    if vybir == "1":
        x = vvesty_x()
        y = obchyslyty_y(x)
        print(f"Результат: y = {y:.6f}")

    elif vybir == "2":
        print("Результат:")
        print(stvoryty_riadok())

    elif vybir == "0":
        print("Програму завершено.")
        break

    else:
        print("Помилка: оберіть 0, 1 або 2.")