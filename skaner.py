class Token:
    def __init__(self, name, value, start_position, length):
        self.name = name
        self.value = value
        self.start_position = start_position
        self.length = length

    def __str__(self):
        return "Nazwa tokenu: " + self.name + "\nWartość: " + self.value


def get_digit_token(input):
    digit_str = ""
    for i in range(0, len(input)):
        if input[i].isdigit():
            digit_str += input[i]
        else:
            break
    return digit_str


def get_bracket_token(input):
    for length, char in enumerate(input):
        if char == ')':
            return length + 1
    raise ValueError("Brak nawiasu zamykającego.")

"""
Zwraca krotkę: (Token, pozycja_końcowa)
"""
def scanner(input, starting_position):
    count_spaces = 0
    for char in input[starting_position:]: # omijamy białe znaki
        if char in (' ', '\n', '\t', '\r'):
            count_spaces += 1
        else:
            break
    starting_position += count_spaces

    if input[starting_position] == ')': # omijamy nawias zamykający
        if '(' not in input[:starting_position]:# to można dopracować
            raise ValueError("Brak nawiasu otwierającego.")
        starting_position += 1

    if input[starting_position].isdigit(): # sprawdzamy czy jest liczbą
        digit = get_digit_token(input[starting_position:])
        ending_position = starting_position + len(digit)
        return Token("liczba_całkowita", digit, starting_position, len(digit)), ending_position

    elif input[starting_position] in ('*', '/', '+', '-'): # sprawdzamy czy jest działaniem
        return Token("działanie", input[starting_position], starting_position, 1), starting_position + 1

    elif input[starting_position] == '(': # sprawdzamy czy jest nawiasem
        length = get_bracket_token(input[starting_position+1:])
        return Token("nawiasy", input[starting_position] + input[starting_position + length],
                    starting_position, 2), starting_position + 1

    else:
        raise ValueError("Zły znak.")


with open("formula.txt", "r", encoding="utf-8") as file:
    input = file.read()


tokens = []
length = 0
while length < len(input) - 1:
    token, length = scanner(input, length)
    tokens.append(token)
for token in tokens:
    print(token)






