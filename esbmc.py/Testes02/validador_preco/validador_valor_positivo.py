MAX_PRICE_LEN: int = 6

def validate_positive_value(price: str, length: int) -> bool:
    value: float = 0.0
    factor: float = 1.0
    after_dot: bool = False
    decimals: int = 0
    i: int = 0

    while i < length:
        c: str = price[i]
        if c == '.':
            after_dot = True
            i += 1
            continue

        value = value * 10 + (ord(c) - ord('0'))

        if after_dot:
            factor *= 10
            decimals += 1

        i += 1

    value /= factor

    assert value > 0, "O preço deve ser um valor positivo."
    return True


def main() -> None:
    price: str = input()        # entrada simbólica
    length: int = len(price)

    # equivalente ao __ESBMC_assume
    assert 1 <= length <= 5

    validate_positive_value(price, length)


main()
