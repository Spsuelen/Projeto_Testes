MAX_PRICE_LEN: int = 6

def validate_length(length: int) -> bool:
    assert 1 <= length <= 5, "Tamanho Incorreto."
    return True


def main() -> None:
    length: int = int(input()) 

    assert 1 <= length <= 5

    validate_length(length)


main()
