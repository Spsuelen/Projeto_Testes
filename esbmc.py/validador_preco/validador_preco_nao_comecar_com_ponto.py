def validate_no_empty_parts(price: str) -> None:
    ESBMC_index: int = 0
    ESBMC_length: int = len(price)
    dot_found: bool = False

    assert not (ESBMC_length > 0 and price[0] == '.')
    assert not (ESBMC_length > 0 and price[ESBMC_length - 1] == '.')

    while ESBMC_index < ESBMC_length:
        char: str = price[ESBMC_index]

        if char == '.':
            assert not dot_found
            dot_found = True
        else:
            dot_found = False

        ESBMC_index += 1

def main() -> None:
    price = ".12"
    validate_no_empty_parts(price)

main()