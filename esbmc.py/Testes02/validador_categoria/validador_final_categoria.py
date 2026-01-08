MAX_LEN: int = 31

def validate_no_end_special_or_digit(category: str, length: int) -> bool:
    specials: str = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`"
    last: str = category[length - 1]

    j: int = 0
    while j < len(specials):
        assert last != specials[j], \
            "A categoria não pode terminar com um número ou caractere especial."
        j += 1

    assert not last.isdigit(), \
        "A categoria não pode terminar com um número ou caractere especial."

    return True


def main() -> None:
    category: str = input()  
    length: int = len(category)

    assert length >= 3 and length <= 30

    validate_no_end_special_or_digit(category, length)


main()
