def validate_category(category: str) -> None:
    specials = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`"
    last_char: str = category[len(category) - 1]

    ESBMC_index: int = 0
    while ESBMC_index < len(specials):
        assert last_char != specials[ESBMC_index]
        ESBMC_index += 1

    assert not ('0' <= last_char <= '9')

def main() -> None:
    category = "Livro1"
    validate_category(category)

main()
