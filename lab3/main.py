
# Тема: Робота зі словником

import math


def read_price():
    """Зчитування ціни журналу з перевіркою помилок."""
    while True:
        value = input("Введіть ціну журналу (грн): ").strip().replace(",", ".")

        try:
            price = float(value)

            if not math.isfinite(price) or price <= 0:
                print("Помилка: ціна має бути додатним скінченним числом.")
                continue

            return price

        except ValueError:
            print("Помилка: введіть числову ціну, наприклад 85 або 85,50.")


def read_circulation():
    """Зчитування тиражу журналу з перевіркою помилок."""
    while True:
        value = input("Введіть тираж журналу (примірників): ").strip()

        try:
            circulation = int(value)

            if circulation <= 0:
                print("Помилка: тираж має бути додатним цілим числом.")
                continue

            return circulation

        except ValueError:
            print("Помилка: тираж потрібно вводити цілим числом, наприклад 9000.")


def add_record(journals):
    """Додавання нового журналу до словника."""
    print("\n--- Додавання журналу ---")

    while True:
        title = input("Введіть назву журналу: ").strip()

        if not title:
            print("Помилка: назва журналу не може бути порожньою.")

        elif any(name.casefold() == title.casefold() for name in journals):
            print("Помилка: журнал із такою назвою вже є у словнику.")

        else:
            break

    price = read_price()
    circulation = read_circulation()

    journals[title] = (price, circulation)
    print(f"Журнал «{title}» успішно додано.")


def print_all_values(journals):
    """Виведення всіх записів словника."""
    if not journals:
        print("\nСловник порожній.")
        return

    print("\n--- Усі журнали ---")

    for title, (price, circulation) in journals.items():
        print(
            f"Журнал: {title} | "
            f"Ціна: {price:.2f} грн | "
            f"Тираж: {circulation} прим."
        )


def remove_record(journals):
    """Видалення запису з обробкою KeyError."""
    if not journals:
        print("\nСловник порожній. Видаляти нічого.")
        return

    print("\n--- Видалення журналу ---")
    title = input("Введіть назву журналу для видалення: ").strip()

    existing_title = next(
        (name for name in journals if name.casefold() == title.casefold()),
        title
    )

    try:
        del journals[existing_title]
        print(f"Журнал «{existing_title}» успішно видалено.")

    except KeyError:
        print(f"Помилка: журнал «{title}» у словнику не знайдено.")


def print_sorted_by_keys(journals):
    """Виведення словника за відсортованими ключами."""
    if not journals:
        print("\nСловник порожній.")
        return

    print("\n--- Журнали за відсортованими ключами ---")

    for title in sorted(journals.keys(), key=str.casefold):
        price, circulation = journals[title]

        print(
            f"Журнал: {title} | "
            f"Ціна: {price:.2f} грн | "
            f"Тираж: {circulation} прим."
        )


def solve_task(journals):
    """Обчислення середньої ціни журналів із тиражем менше 10000."""
    if not journals:
        print("\nСловник порожній. Обчислення неможливе.")
        return

    selected = [
        (title, price)
        for title, (price, circulation) in journals.items()
        if circulation < 10000
    ]

    if not selected:
        print("\nЖурналів із тиражем менше 10000 примірників немає.")
        return

    print("\n--- Журнали з тиражем менше 10000 примірників ---")

    for title, price in selected:
        print(f"{title}: {price:.2f} грн")

    average_price = sum(price for _, price in selected) / len(selected)

    print(f"Кількість журналів: {len(selected)}")
    print(f"Середня вартість журналів: {average_price:.2f} грн")


def main():

        journals = {}

        print("=== РОБОТА ЗІ СЛОВНИКОМ ===")
        print("Введіть дані про 5 журналів.")

        for number in range(1, 6):
            print(f"\nЖурнал {number} із 5:")
            add_record(journals)

        print("\n=== ГОЛОВНЕ МЕНЮ ===")
        print("1. Вивести всі записи словника")
        print("2. Додати новий журнал")
        print("3. Видалити журнал")
        print("4. Переглянути словник за відсортованими ключами")
        print("5. Обчислити середню ціну журналів із тиражем менше 10000")
        print("0. Завершити програму")

        while True:
            choice = input(
                "\nОберіть наступну дію з меню вище (0–5): "
            ).strip()

            if choice == "1":
                print_all_values(journals)

            elif choice == "2":
                add_record(journals)

            elif choice == "3":
                remove_record(journals)

            elif choice == "4":
                print_sorted_by_keys(journals)

            elif choice == "5":
                solve_task(journals)

            elif choice == "0":
                print("Роботу програми завершено.")
                break

            else:
                print("Помилка: оберіть номер від 0 до 5.")

if __name__ == "__main__":
    main()
