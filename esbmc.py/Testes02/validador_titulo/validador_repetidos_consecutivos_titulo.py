MAX_LEN_TITLE: int = 21

def validate_consecutive_repeated(title: str, length: int) -> bool:
    i: int = 0
    while i < length - 1:
        assert title[i] != title[i + 1], \
            "O título não deve conter caracteres repetidos consecutivos."
        i += 1
    return True


def main() -> None:
    title: str = input()      
    length: int = len(title)

    assert 1 <= length <= 20  

    validate_consecutive_repeated(title, length)


main()
