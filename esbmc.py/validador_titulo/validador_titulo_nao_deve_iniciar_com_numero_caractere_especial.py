def validate_title(title: str) -> None:
    specials = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`"
    first_char: str = title[0]
    ESBMC_index: int = 0
    while ESBMC_index < len(specials):
        assert first_char != specials[ESBMC_index]
        ESBMC_index += 1
    assert not ('0' <= first_char <= '9')

def main() -> None:
    title = "@Livro"
    validate_title(title)

main()
