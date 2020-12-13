def is_isogram(string):
    a = list(string.lower())
    while " " in a:
        a.remove(" ")
    while "-" in a:
        a.remove("-")
    for ix in a:
        b = a.count(ix)
        if b > 1:
            return False
    return True
