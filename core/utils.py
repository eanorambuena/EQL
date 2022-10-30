def numberize(value):
    """Converts a string to a number, if possible."""
    if type(value) == str:
        if value.isnumeric():
            value = int(value)
        elif value.split('.')[0].isnumeric() and value.split('.')[1].isnumeric():
            value = float(value)
    return value
