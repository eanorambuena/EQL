def numberize(value):
    """Converts a string to a number, if possible."""
    if type(value) == str:
        value: str = value
        abs_value = value.lstrip("-")
        if abs_value.isnumeric():
            value = int(value)
        elif abs_value.split('.')[0].isnumeric() and abs_value.split('.')[1].isnumeric():
            value = float(value)
    return value
