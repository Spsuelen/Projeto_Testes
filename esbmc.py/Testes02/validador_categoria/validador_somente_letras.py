MAX_LEN: int = 31

def validate_only_letters(category: str, length: int) -> bool:
    i: int = 0
    while i < length:
        assert category[i].isalpha(), \
            "A categoria deve conter apenas letras (sem números)."
        i += 1
    return True


def main() -> None:
    category: str = input() 
    length: int = len(category)
    
    assert length >= 3 and length <= 30

    validate_only_letters(category, length)


main()
