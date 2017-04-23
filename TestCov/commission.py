def Commission(l, s, b):
    if l not in range(-1, 71) or l == 0 or s not in range(1, 81) or b not in range(1, 91):
        return "InvalidInput"
    elif l == -1:
        return "ProgramTerminates"

    sales = l * 45 + s * 30 + b * 25

    if sales >= 1800:
        comm = 0.1 * 1000 + 0.15 * 800 + 0.2 * (sales - 1800)
    elif sales >= 1000:
        comm = 0.1 * 1000 + 0.15 * (sales - 1000)
    else:
        comm = 0.1 * sales

    return "${:0,.2f}".format(comm).rstrip("0").rstrip(".")
