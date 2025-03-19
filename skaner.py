class Token:
    def __init__(self, name, value, start_position, length):
        self.name = name
        self.value = value
        self.start_position = start_position
        self.length = length

    def __str__(self):
        return "Nazwa tokenu: " + self.name + "\nWartość: " + self.value


def get_digit_token(input, starting_position):
    digit_str = ""
    for i in range(0, len(input)):
        if input[i].isdigit():
            digit_str += input[i]
        else:
            break
    return Token("liczba_całkowita", digit_str,
                                     starting_position, len(digit_str))


def get_bracket_token(input, starting_position):
    for length, char in enumerate(input[starting_position + 1:]):
        if char == ')':
            return Token("nawiasy", input[starting_position] + input[starting_position + length + 1],
                         starting_position, length + 1)
    raise ValueError("Brak nawiasu zamykającego.")


def get_token(input, starting_position):
    if input[starting_position] == ' ':
        starting_position += 1
    if input[starting_position].isdigit():
        return get_digit_token(input, starting_position)
    elif input[starting_position] in ('*', '/', '+', '-'):
        return Token("działanie", input[starting_position], starting_position, 1)
    elif input[starting_position] == '(':
        return get_bracket_token(input, starting_position)
    elif input[starting_position] == ')':
        if '(' not in input[:starting_position]:
            raise ValueError("Brak nawiasu otwierającego.")
    else:
        raise ValueError("Zły znak.")


with open("formula.txt", "r", encoding="utf-8") as file:
    input = file.read()

token1 = get_token(input, 0)
print(token1)





