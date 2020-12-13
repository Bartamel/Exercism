import re
def abbreviate(words):
    a = re.split(" |-", words)
    b = ""
    while "" in a:
        a.remove("")
    for i in a:
        i = i.replace("_", "")
        b = b + i[0]
    return b.upper()
