def validate_title(title: str) -> None:
    ESBMC_index: int = 0
    ESBMC_length: int = len(title)
    while ESBMC_index < ESBMC_length:
        char: str = title[ESBMC_index]
        assert ('a' <= char <= 'z') or ('A' <= char <= 'Z')
        ESBMC_index += 1

def main() -> None:
    title = "Livro"
    validate_title(title)

main()
