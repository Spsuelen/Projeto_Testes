MAX_LEN: int = 31

def is_letter(c: str) -> bool:
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z')

def validate_category(category: str, length: int) -> bool:
    specials: str = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`"

    assert 3 <= length <= 30, "A categoria deve ter entre 3 e 30 caracteres."

    assert is_letter(category[0]), "A categoria deve começar com uma letra."

    i: int = 0
    while i < length - 1:
        assert category[i] != category[i + 1], \
            "A categoria não deve conter caracteres repetidos consecutivos."
        i += 1

    i = 0
    while i < length:
        c: str = category[i]
        assert c != ' ', "A categoria não deve conter espaços."
        assert is_letter(c), "A categoria deve conter apenas letras (sem números)."
        
        j: int = 0
        while j < len(specials):
            assert c != specials[j], "A categoria não deve conter caracteres especiais."
            j += 1
        i += 1

    last: str = category[length - 1]
    assert not ('0' <= last <= '9') and last not in specials, \
        "A categoria não pode terminar com um número ou caractere especial."

    return True

def main() -> None:
    category: str = input()
    length: int = len(category)

    assert 3 <= length <= 30

    validate_category(category, length)

main()