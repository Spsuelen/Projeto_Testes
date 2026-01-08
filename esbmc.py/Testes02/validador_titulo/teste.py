MAX_LEN_TITLE: int = 21

def validate_only_letters(title: str, length: int) -> bool:
    i: int = 0
    while i < length:
        assert title[i].isalpha(), "O título deve conter apenas letras."
        i += 1
    return True

def validate_no_spaces(title: str, length: int) -> bool:
    i: int = 0
    while i < length:
        assert title[i] != ' ', "O título não deve conter espaços."
        i += 1
    return True

def validate_consecutive_repeated(title: str, length: int) -> bool:
    i: int = 0
    while i < length - 1:
        assert title[i] != title[i + 1], \
            "O título não deve conter caracteres repetidos consecutivos."
        i += 1
    return True

def validate_not_only_spaces(title: str, length: int) -> bool:
    only_spaces: bool = True
    i: int = 0
    while i < length:
        if title[i] != ' ':
            only_spaces = False
            break
        i += 1
    assert not only_spaces, "O título não pode ser apenas espaços."
    return True

def validate_no_start_with_number_or_special(title: str, length: int) -> bool:
    specials: str = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`"
    assert not ('0' <= title[0] <= '9'), \
        "O título não pode começar com um número ou caractere especial."
    j: int = 0
    while j < len(specials):
        assert title[0] != specials[j], \
            "O título não pode começar com um número ou caractere especial."
        j += 1
    return True

def validate_no_special_characters(title: str, length: int) -> bool:
    specials: str = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`"
    i: int = 0
    while i < length:
        j: int = 0
        while j < len(specials):
            assert title[i] != specials[j], \
                "O título não deve conter caracteres especiais."
            j += 1
        i += 1
    return True

def validate_length(len_title: int) -> bool:
    assert 1 <= len_title <= 20, "Tamanho ou caracteres inválidos."
    return True

def main() -> None:
    title: str = input()
    length: int = len(title)

    validate_length(length)
    validate_not_only_spaces(title, length)
    validate_no_start_with_number_or_special(title, length)
    validate_no_spaces(title, length)
    validate_no_special_characters(title, length)
    validate_only_letters(title, length)
    validate_consecutive_repeated(title, length)

main()