
MAX_LEN: int = 31

def validate_start_with_letter(category: str) -> bool:
    assert category[0].isalpha(), "A categoria deve começar com uma letra."
    return True


def main() -> None:
    category: str = input()   
    length: int = len(category)

    
    assert length >= 3 and length <= 30
    assert 32 <= ord(category[0]) <= 126   

    validate_start_with_letter(category)


main()
