def validate_price(price: str):
 
    assert price.strip() != "", "O preço não pode conter apenas espaços."

def main() -> None:
    price = "    "  
    validate_price(price)

main()
