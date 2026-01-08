MAX_LEN: int = 31

def validate_consecutive_repeated(category: str, length: int) -> bool:
    i: int = 0
    while i < length - 1:
        assert category[i] != category[i + 1], \
            "A categoria não deve conter caracteres repetidos consecutivos."
        i += 1
    return True


def main() -> None:
    category: str = input()  
    length: int = len(category)

    assert length >= 3 and length <= 30

    validate_consecutive_repeated(category, length)


main()
