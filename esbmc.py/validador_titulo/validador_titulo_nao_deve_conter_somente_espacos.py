def validate_title(title: str) -> None:
    ESBMC_index: int = 0
    ESBMC_length: int = len(title)
    only_spaces = True
    while ESBMC_index < ESBMC_length:
        char: str = title[ESBMC_index]
        if char != ' ':
            only_spaces = False
        ESBMC_index += 1
    assert not only_spaces

def main() -> None:
    title = "titulo"
    validate_title(title)

main()
