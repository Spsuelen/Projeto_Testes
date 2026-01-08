MAX_LEN: int = 31

def validate_no_spaces(category: str, length: int) -> bool:
    i: int = 0
    while i < length:
        assert category[i] != ' ', "A categoria não deve conter espaços."
        i += 1
    return True


def main() -> None:
    category: str = input()      
    length: int = len(category)  

    assert length >= 3 and length <= 30

    validate_no_spaces(category, length)


main()
