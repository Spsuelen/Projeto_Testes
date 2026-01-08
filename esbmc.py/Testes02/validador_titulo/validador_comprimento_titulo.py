MAX_LEN_TITLE: int = 21

def validate_length(len_title: int) -> bool:
    assert 1 <= len_title <= 20, "Tamanho ou caracteres inválidos."
    return True

def main() -> None:
    len_title: int = int(input()) 
    assert 1 <= len_title <= 20     

    validate_length(len_title)

main()
