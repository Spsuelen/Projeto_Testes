def validate_price(price: str):
    parts = price.split('.')
    assert len(parts[0]) <= 5 and parts[0].isdigit(), "A parte inteira deve ter até 5 dígitos e conter apenas números."
    assert len(parts) == 2 and len(parts[1]) == 2 and parts[1].isdigit(), "A parte decimal deve conter exatamente 2 dígitos numéricos."
    valor = float(price)
    assert 1 <= valor <= 99999.99, "O preço deve estar entre 1 e 99999.99."

def main() -> None:
    price = "12345.67"  
    validate_price(price)

main()
