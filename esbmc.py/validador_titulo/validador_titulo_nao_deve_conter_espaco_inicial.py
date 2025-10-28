MAX_LEN = 20

def validate_title(title: str) -> None:
    ESBMC_index: int = 0
    ESBMC_length: int = len(title)

    while ESBMC_index < ESBMC_length:
        if ESBMC_index == 0:
            assert title[ESBMC_index] != ' ', "O título não deve começar com espaço."
        ESBMC_index += 1

def main() -> None:
    title = " Livro"
    validate_title(title)

main()
