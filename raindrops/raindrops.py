def convert(number):
    if number % 3 == 0:
        r = "Pling"
        if number % 5 == 0:
            r = r + "Plang"
        if number % 7 == 0:
            r = r + "Plong"
    elif number % 5 == 0:
        r = "Plang"
        if number % 7 == 0:
            r = r + "Plong"
    elif number % 7 == 0:
        r = "Plong"
    else:
        r = str(number)
    return r
