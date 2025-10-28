def validate_single_dot(price: str) -> None:
    i = 0
    dots = 0
    while i < len(price):
        if price[i] == '.':
            dots += 1
            if dots > 1:
                raise AssertionError("Erro: Mais de um ponto decimal não é permitido.")
        i += 1

def main() -> None:
    price = "12.3.4"
    validate_single_dot(price)

main()
