MAX_PRICE_LEN: int = 6

def validate_characters(price: str, length: int) -> bool:
    dot_count: int = 0
    i: int = 0
    while i < length:
        c: str = price[i]
        if c == '.':
            dot_count += 1
        else:
            assert c.isdigit(), "O preço deve conter apenas números e, no máximo, um ponto."
        i += 1
    assert dot_count <= 1, "O preço não pode conter mais de um ponto."
    return True


def main() -> None:
    price: str = input()          
    length: int = len(price)

    assert length >= 1 and length <= 5

    validate_characters(price, length)


main()
