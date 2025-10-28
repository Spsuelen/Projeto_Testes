MAX_LEN = 20
def validate_title(title: str):
    for char in title:
        assert char.isalpha(), "O título deve conter apenas letras."
def main() -> None:
    title = "Livro"
    validate_title(title)
main()
