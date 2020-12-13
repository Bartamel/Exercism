def score(word):
    one_point = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t",
                 "A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    two_point = ["d", "g", "D", "G"]
    three_point = ["b", "c", "m", "p", "B", "C", "M", "P"]
    four_point = ["f", "h", "v", "w", "y", "F", "H", "V", "W", "Y"]
    five_point = ["k", "K"]
    eight_point = ["j", "x", "J", "X"]
    ten_point = ["q", "z", "Q", "Z"]
    points = 0
    for i in word:
        if i in one_point:
            points += 1
        if i in two_point:
            points += 2
        if i in three_point:
            points += 3
        if i in four_point:
            points += 4
        if i in five_point:
            points += 5
        if i in eight_point:
            points += 8
        if i in ten_point:
            points += 10
    return points
