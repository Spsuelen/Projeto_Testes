def validate_no_letters(price: str) -> None:
    ESBMC_index: int = 0
    ESBMC_length: int = len(price)

    while ESBMC_index < ESBMC_length:
        char: str = price[ESBMC_index]

        assert not ('a' <= char and char <= 'z')
        assert not ('A' <= char and char <= 'Z')

        ESBMC_index += 1

def main() -> None:
    price = "123a"
    validate_no_letters(price)
main()