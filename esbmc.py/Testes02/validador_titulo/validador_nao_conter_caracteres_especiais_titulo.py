MAX_LEN_TITLE: int = 21

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


def main() -> None:
    title: str = input()          
    length: int = len(title)

    assert 1 <= length <= 20   

    validate_no_special_characters(title, length)


main()
