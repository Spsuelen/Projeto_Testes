def validate_title(title: str) -> None:
    ESBMC_index: int = 0
    ESBMC_length: int = len(title) - 1
    while ESBMC_index < ESBMC_length:
        assert not (title[ESBMC_index] == ' ' and title[ESBMC_index + 1] == ' ')
        ESBMC_index += 1

def main() -> None:
    title = "Livro  Antigo"
    validate_title(title)

main()
