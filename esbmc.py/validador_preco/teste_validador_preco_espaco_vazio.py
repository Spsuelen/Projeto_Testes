def validate_price(price: str):

    assert price != "", "O preço não pode ser vazio."

def main() -> None:
    price = ""  
    validate_price(price)

main()
