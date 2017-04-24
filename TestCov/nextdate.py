def NextDate(m, d, y):
    # Add constraint for vailid date
    if m not in range(1, 13) or d not in range(1, 32) or y not in range(1812, 2013):
        return "InvalidInput"

    # Differenciate big/small month and leap/common year
    if m in [1, 3, 5, 7, 8, 10, 12]:
        edgeday = 31
    elif m == 2 and (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
        edgeday = 29
    elif m == 2:
        edgeday = 28
    else:
        edgeday = 30

    # Validate the day
    if d > edgeday:
        return "InvalidInput"

    # Calculate next date
    if d + 1 > edgeday:
        if m + 1 > 12:
            if y + 1 > 2012:
                return "InvalidInput"
            else:
                y += 1
                m = 1
                d = 1
        else:
            m += 1
            d = 1
    else:
        d += 1

    return "{}.{}.{}".format(m, d, y)
