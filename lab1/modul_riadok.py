def stvoryty_riadok():
    ryadok = ""

    for pozytsiya in range(1, 21):
        if pozytsiya % 3 == 0:
            ryadok += "?"
        else:
            ryadok += "*"

    return ryadok