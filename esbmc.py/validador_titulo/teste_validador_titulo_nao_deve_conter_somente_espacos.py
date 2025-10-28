CARACTERES_ESPECIAIS_INVALIDOS = '!@#$%^&*()_+=-[]{}|;:,.<>?/~`'
def validate_title_start(title: str) -> None:
    first_char = title[0]

    is_digit = first_char.isdigit()
    assert not is_digit, "O título não pode começar com um número."

    is_special_char = first_char in CARACTERES_ESPECIAIS_INVALIDOS
    assert not is_special_char, "O título não pode começar com um caractere especial."

def main() -> None:
    title = "1Livro"
    validate_title_start(title)

main()