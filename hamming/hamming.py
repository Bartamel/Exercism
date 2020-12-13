def distance(strand_a, strand_b):
    a = 0
    diference = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Is not the same length")
    else:
        for i in strand_a:
            if i != strand_b[a]:
                diference += 1
            a += 1
    return diference
