class Token:
    def __init__(self, name, value, start_position, length):
        self.name = name
        self.value = value
        self.start_position = start_position
        self.length = length

    def __str__(self):
        return "Nazwa tokenu: " + self.name + "\nWartość: " + self.value + "\nKolumna: " + str(self.start_position)


def get_int_token(input):
    digit_str = str(input[0])
    for i in range(1, len(input)):
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


def get_full_word(input):
    word = ""
    for i in range(0, len(input)):
        if input[i].isalnum() or input[i] == "_":
            word += input[i]
        else:
            break
    return word


def get_whole_line(input):
    line = ""
    for i in range(0, len(input)):
        if input[i] != "\n":
            line += input[i]
        else:
            break
    return line


def get_string(input):
    str = ""
    for i in range(0, len(input)):
        if input[i] != "\"":
            str += input[i]
        else:
            return str
    raise ValueError("Brak pełnego cudzysłowu.")

def get_float_token(input):
    number = ""
    dot_seen = False
    
    for i, char in enumerate(input):
        if char.isdigit():
            number += char
        elif char == "." and not dot_seen:
            number += char
            dot_seen = True
        else:
            break
    
    if number.count(".") == 1 and len(number) > 1:
        return number
    return None


KEYWORDS = ["import", "range", "def", "if", "else", "break", "in", "not", "return", "raise", "for", "try", "while", "except", "len",
            "True", "False", "print"]
SINGLE_OPERATORS = ["=", "+", "-", "/", "*", ">", "<"]
DOUBLE_OPERATORS = ["+=", "-=", "==", "//", "**", "<=", ">="]
BRACKETS = ["(", ")", "[", "]", "{", "}"]
SPECIAL_SIGNS = [".", ",", ":"]
WHITE_SIGNS = [' ', '\n', '\t', '\r']


def scanner(input, starting_position):

    if starting_position >= len(input):
        raise ValueError(f"Błąd: Nieoczekiwany koniec wejścia w kolumnie {starting_position}.")

    if input[starting_position] in WHITE_SIGNS:
        return Token("znak_bialy", input[starting_position], starting_position, 1), starting_position + 1

    if input[starting_position] == '#':
        comment = get_whole_line(input[starting_position:])
        ending_position = starting_position + len(comment)
        return Token("komentarz", comment, starting_position, len(comment)), ending_position

    if input[starting_position] in ("\"", "\'"):
        string_value = "\"" + get_string(input[starting_position+1:]) + "\""
        ending_position = starting_position + len(string_value)
        return Token("string", string_value, starting_position, len(string_value)), ending_position

    if input[starting_position].isalpha() or input[starting_position] == "_":
        word = get_full_word(input[starting_position:])
        ending_position = starting_position + len(word)
        if word in KEYWORDS:
            return Token("keyword", word, starting_position, len(word)), ending_position
        return Token("nazwa_zmiennej", word, starting_position, len(word)), ending_position

    if input[starting_position] in SINGLE_OPERATORS: # sprawdzamy czy jest działaniem
        if input[starting_position] + input[starting_position+1] in DOUBLE_OPERATORS:
            return Token("double_operators", input[starting_position] + input[starting_position+1], starting_position, 2), starting_position + 2
        return Token("single_operators", input[starting_position], starting_position, 1), starting_position + 1

    if input[starting_position] in BRACKETS: # sprawdzamy czy jest nawiasem
        try:
            return Token("bracket", input[starting_position], starting_position, 1), starting_position + 1
        except ValueError as e:
            raise ValueError(f"{str(e)} w kolumnie {starting_position}.")

    if input[starting_position] in SPECIAL_SIGNS:
        return Token("znak_specjalny", input[starting_position], starting_position, 1), starting_position + 1

    if input[starting_position].isdigit() or (input[starting_position] == '-' and input[starting_position+1].isdigit()):
        float_value = get_float_token(input[starting_position:])
        if float_value:
            return Token("float", float_value, starting_position, len(float_value)), starting_position + len(float_value)

    digit = get_int_token(input[starting_position:])
    return Token("int", digit, starting_position, len(digit)), starting_position + len(digit)

    raise ValueError(f"Błąd: Nieznany znak '{input[starting_position]}' w kolumnie {starting_position}.")







