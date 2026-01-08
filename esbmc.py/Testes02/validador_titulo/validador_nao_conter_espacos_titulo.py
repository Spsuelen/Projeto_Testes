MAX_LEN_TITLE: int = 21

def validate_no_spaces(title: str, length: int) -> bool:
    i: int = 0
    while i < length:
        assert title[i] != ' ', "O título não deve conter espaços."
        i += 1
    return True


def main() -> None:
    title: str = input()      
    
    length: int = len(title)

    assert 1 <= length <= 20 
    
    validate_no_spaces(title, length)


main()
