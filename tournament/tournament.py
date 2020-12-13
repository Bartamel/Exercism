from tabulate import tabulate
def tally(rows):
    print(rows)
    games = len(rows)
    count = 1
    data = []
    teams = []
    winner = []
    loser = []
    ties = []
    result = []
    headers =["Team", "MP", "W", "D", "L", "P"]
    while count < games:
        a = rows[count]
        data = a.split(';')
        for i in range(0, 1):
            if data[i] not in teams:
                teams.append(data[i])
        if data[2] == "win":
            winner = data[0]
            loser = data[1]
        if data[2] == "lose":
            winner = data[1]
            loser = data[0]
        if data[2] == "draw":
            ties.append(data[0])
            ties.append(data[1])
        count += 1
    for j in teams:
        win = 0
        lose = 0
        draw = 0
        played = 0
        points = 0
        fila = []
        win = winner.count(j)
        lose = loser.count(j)
        draw = ties.count(j)
        played = win + lose + draw
        points = (win*3) + (draw)
        fila = [j, played, win, draw, lose, points]
        result.append(fila)
    return tabulate(result, headers=headers, stralign= "left")
