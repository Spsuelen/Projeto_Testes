def validate_title(title: str) -> None:
    specials = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`"
    ESBMC_index: int = 0
    ESBMC_length: int = len(title)
    while ESBMC_index < ESBMC_length:
        char: str = title[ESBMC_index]
        ESBMC_j: int = 0
        while ESBMC_j < len(specials):
            assert char != specials[ESBMC_j]
            ESBMC_j += 1
        ESBMC_index += 1

def main() -> None:
    title = "Livro$"
    validate_title(title)

main()
