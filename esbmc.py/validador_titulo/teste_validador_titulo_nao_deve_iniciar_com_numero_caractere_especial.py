caracteres_especiais_invalidos = '!@#$%^&*()_+=-[]{}|;:,.<>?/~`'
def validate_title(title: str)-> None:
    first = title[0]
    assert not first.isdigit()
    assert first not in caracteres_especiais_invalidos
def main() -> None:
    title = "1Livro"
    validate_title(title)

main()
