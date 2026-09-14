def znaity_naichastishi_cyfry(cyfry):
    mnozhyna = set(cyfry)
    rezultat = set()
    maks_kilkist = 0

    for cyfra in mnozhyna:
        kilkist = cyfry.count(cyfra)

        if kilkist > maks_kilkist:
            maks_kilkist = kilkist
            rezultat = {cyfra}
        elif kilkist == maks_kilkist:
            rezultat.add(cyfra)

    return rezultat, maks_kilkist


print("ЗАВДАННЯ 3.")

while True:
    vvedennya = input("Введіть цифри від 0 до 9 через пробіл: ").split()

    if len(vvedennya) == 0:
        print("Помилка: потрібно ввести хоча б одну цифру.")
        continue

    pravilno = True

    for element in vvedennya:
        if not element.isdigit() or len(element) != 1:
            pravilno = False
            break

    if pravilno:
        cyfry = [int(element) for element in vvedennya]
        break
    else:
        print("Помилка: вводьте тільки цифри від 0 до 9.")


rezultat, kilkist = znaity_naichastishi_cyfry(cyfry)

print("Цифри, яких у наборі найбільше:")
print(rezultat)
print(f"Кількість повторень: {kilkist}")