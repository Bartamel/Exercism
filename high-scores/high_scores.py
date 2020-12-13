def latest(scores):
    menor = scores[0]
    for i in scores:
        if (i < menor) and (i > 0):
            menor = i
    return menor


def personal_best(scores):
    mayor = max(scores)
    return mayor


def personal_top_three(scores):
    top_three = sorted(scores, reverse= True)[:3]
    return top_three
