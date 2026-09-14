def otrymaty_slova(rechennya):
    znaky = ".,!?;:()[]{}\"«»"
    slova = []

    for slovo in rechennya.split():
        chyste_slovo = slovo.strip(znaky)

        if chyste_slovo:
            slova.append(chyste_slovo)

    return slova


def pereviryty_naidovshe(slova):
    naidovshe = max(slova, key=len)

    if len(naidovshe) > 10:
        return True, naidovshe
    else:
        return False, naidovshe


print("ЗАВДАННЯ 1.")

while True:
    rechennya = input("Введіть речення щонайменше із 7 слів: ")
    slova = otrymaty_slova(rechennya)

    if len(slova) < 7:
        print("Помилка: речення повинно містити щонайменше 7 слів.")
    else:
        break


pravda, naidovshe = pereviryty_naidovshe(slova)

if pravda:
    print("Твердження правдиве.")
    print(f"Найдовше слово: {naidovshe}")
else:
    print("Твердження неправдиве.")