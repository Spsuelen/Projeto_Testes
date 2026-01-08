MAX_LEN_TITLE: int = 21

def validate_no_start_with_number_or_special(title: str, length: int) -> bool:
    specials: str = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`"

    assert not ('0' <= title[0] <= '9'), \
        "O título não pode começar com um número ou caractere especial."

    
    j: int = 0
    while j < len(specials):
        assert title[0] != specials[j], \
            "O título não pode começar com um número ou caractere especial."
        j += 1

    return True

def main() -> None:
   
    title: str = input()
    length: int = len(title)

    assert 1 <= length <= 20 

    validate_no_start_with_number_or_special(title, length)

main()