def validate_category(category: str) -> None:
    first_char: str = category[0]
    assert (('a' <= first_char <= 'z') or ('A' <= first_char <= 'Z'))

def main() -> None:
    category = "livr1"
    validate_category(category)

main()
