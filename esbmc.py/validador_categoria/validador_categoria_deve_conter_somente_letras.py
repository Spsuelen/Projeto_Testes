def validate_category(category: str) -> None:
    specials = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`"
    ESBMC_index: int = 0
    ESBMC_length: int = len(category)
    while ESBMC_index < ESBMC_length:
        char: str = category[ESBMC_index]
        ESBMC_j: int = 0
        while ESBMC_j < len(specials):
            assert char != specials[ESBMC_j]
            ESBMC_j += 1
        assert (('a' <= char <= 'z') or ('A' <= char <= 'Z'))
        ESBMC_index += 1

def main() -> None:
    category = "Livro"
    validate_category(category)

main()
