def validate_category(category: str) -> None:
    ESBMC_index: int = 0
    ESBMC_length: int = len(category)

    assert (ESBMC_length >= 3 and ESBMC_length <= 30)
    while ESBMC_index < ESBMC_length:
        char: str = category[ESBMC_index]
        assert (('a' <= char <= 'z') or ('A' <= char <= 'Z'))
        ESBMC_index += 1
        
def main() -> None:
    category = "oi"
    validate_category(category)
    
main()
