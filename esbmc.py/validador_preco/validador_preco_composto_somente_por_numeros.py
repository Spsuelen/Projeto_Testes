def validate_is_number(price: str) -> None:
    dot_found: bool = False
    ESBMC_index: int = 0
    ESBMC_length: int = len(price)

    while ESBMC_index < ESBMC_length:
        char: str = price[ESBMC_index]

        if char == '.':
            assert not dot_found
            dot_found = True
        else:
            assert '0' <= char
            assert char <= '9'

        ESBMC_index += 1

def main() -> None:
    price = "abc"
    validate_is_number(price)

main()