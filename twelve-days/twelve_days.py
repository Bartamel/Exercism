def recite(start_verse, end_verse):
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
           "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    gitf = ["a Partridge in a Pear Tree.", "two Turtle Doves",
            "three French Hens", "four Calling Birds", "five Gold Rings",
            "six Geese-a-Laying", "seven Swans-a-Swimming",
            "eight Maids-a-Milking", "nine Ladies Dancing",
            "ten Lords-a-Leaping", "eleven Pipers Piping",
            "twelve Drummers Drumming"]
    final = end_verse
    count = start_verse - 1
    salida = []
    while count < final:
        start = gitf[0]
        complement = ""
        for i in range(count, 0, -1):
            complement += gitf[i]+", "
        if count == 0:
            output = start
        else:
            output = complement + "and " + start
        out = f"On the {day[count]} day of Christmas my true love gave to me: " + output
        salida.append(out)
        count += 1
    return salida
