def validate_title(title: str) -> None:
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    first_char: str = title[0]

    ESBMC_index: int = 0
    found: bool = False
    while ESBMC_index < len(letters):
        if first_char == letters[ESBMC_index]:
            found = True
        ESBMC_index += 1
    assert found

def main() -> None:
    title = "Livro"
    validate_title(title)

main()
