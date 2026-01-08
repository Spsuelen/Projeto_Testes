MAX_LEN_TITLE: int = 21

def validate_not_only_spaces(title: str, length: int) -> bool:
    only_spaces: bool = True
    
    i: int = 0
    while i < length:
        if title[i] != ' ':
            only_spaces = False
            break
        i += 1

    assert not only_spaces, "O título não pode ser apenas espaços."
    return True


def main() -> None:
    title: str = input()    
    length: int = len(title)

    assert 1 <= length <= 20  

    validate_not_only_spaces(title, length)


main()