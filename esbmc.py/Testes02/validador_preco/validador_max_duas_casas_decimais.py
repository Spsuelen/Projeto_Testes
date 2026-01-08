MAX_PRICE_LEN: int = 6

def validate_max_two_decimal_places(price: str, length: int) -> bool:
    dot_count: int = 0
    decimals: int = 0
    i: int = 0

    while i < length:
        c: str = price[i]
        if c == '.':
            dot_count += 1
        if dot_count == 1 and c.isdigit():
            decimals += 1
        i += 1

    assert decimals <= 2, "O preço não pode ter mais de duas casas decimais."
    return True


def main() -> None:
    price: str = input()
    length: int = len(price)

    assert 1 <= length <= 5

    validate_max_two_decimal_places(price, length)


main()
