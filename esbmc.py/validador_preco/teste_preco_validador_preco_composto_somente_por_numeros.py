def validate_is_number(price: str) -> None:
    dot_found = False
    for c in price:
        if c == '.':
            if dot_found:
                raise AssertionError("Erro: O valor não é um número válido (mais de um ponto).")
            dot_found = True
        elif not ('0' <= c <= '9'):
            raise AssertionError("Erro: O valor não é um número válido (caractere inválido).")

def main() -> None:
    price = "abc"
    validate_is_number(price)

main()
