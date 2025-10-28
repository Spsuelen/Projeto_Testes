def validate_price(price: str) -> None:
    ESBMC_index: int = 0
    ESBMC_length: int = len(price)
    has_non_space: bool = False

    while ESBMC_index < ESBMC_length:
        char: str = price[ESBMC_index]
        
        if not (char == ' ' or char == '\t' or char == '\n' or char == '\r'):
            has_non_space = True
            
        ESBMC_index += 1
    
    assert has_non_space

def main() -> None:
    price = "    " 
    validate_price(price)

main()