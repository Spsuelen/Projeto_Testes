MAX_LEN_TITLE: int = 21

def validate_only_letters(title: str, length: int) -> bool:
    i: int = 0
    while i < length:
        assert title[i].isalpha(), "O título deve conter apenas letras."
        i += 1
    return True


def main() -> None:
    title: str = input()      
    length: int = len(title)

    assert 1 <= length <= 20  

    validate_only_letters(title, length)


main()
