def checkio(data):
    if len(data) == 1:
        return data[0]
    else:
        return data[0] + checkio(data[1:])


checkio([1, 2, 3])
