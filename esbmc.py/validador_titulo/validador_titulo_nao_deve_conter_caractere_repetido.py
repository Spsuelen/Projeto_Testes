def validate_title(title: str) -> None:
    ESBMC_index: int = 0
    ESBMC_length: int = len(title) - 1

    while ESBMC_index < ESBMC_length:
        current_char: str = title[ESBMC_index]
        next_char: str = title[ESBMC_index + 1]
        assert current_char != next_char
        ESBMC_index += 1

def main() -> None:
    title = "Livroooo"
    validate_title(title)

main()
