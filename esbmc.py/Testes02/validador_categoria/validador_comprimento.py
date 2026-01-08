MAX_LEN: int = 31

def validate_length(length: int) -> bool:
    assert length >= 3 and length <= 30, \
        "A categoria deve ter entre 3 e 30 caracteres."
    return True


def main() -> None:
    category: str = input()        
    length: int = len(category)   

    assert length >= 3 and length <= 30

    validate_length(length)


main()
