def validate_price(price: str)-> None:
    value = float(price)  
    assert value < 0, "O preço deve ser um valor negativo."

def main() -> None:
    price = "-500.00"
    validate_price(price)

main()
