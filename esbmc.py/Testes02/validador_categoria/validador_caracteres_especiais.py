MAX_LEN: int = 31

def validate_no_special_characters(category: str, length: int) -> bool:
    specials: str = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`"
    i: int = 0
    while i < length:
        j: int = 0
        while j < len(specials):
            assert category[i] != specials[j], \
                "A categoria não deve conter caracteres especiais."
            j += 1
        i += 1
    return True


def main() -> None:
    category: str = input()    
    length: int = len(category)
    
    assert length >= 3 and length <= 30

    validate_no_special_characters(category, length)


main()
