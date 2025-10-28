def validate_category(category: str) -> None:
    first_char: str = category[0]
    assert first_char != ' '

def main() -> None:
    category = " ajeitar a tv"
    validate_category(category)

main()
