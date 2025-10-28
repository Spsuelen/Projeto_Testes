def validate_category(category: str) -> None:
    last_char: str = category[len(category) - 1]
    assert last_char != ' '

def main() -> None:
    category = "ajeitar a internet"
    validate_category(category)

main()
