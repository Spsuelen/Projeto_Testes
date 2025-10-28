def validate_category(category: str) -> None:
    ESBMC_index: int = 0
    ESBMC_length: int = len(category)
    while ESBMC_index < ESBMC_length - 1:
        char: str = category[ESBMC_index]
        next_char: str = category[ESBMC_index + 1]
        assert char != next_char
        ESBMC_index += 1

def main() -> None:
    category = "Livross" 
    validate_category(category)

main()
