def validate_category(category: str):
    for char in category:
        assert char.isalpha()

def main() -> None:
    category = "Livro"
    validate_category(category)

main()
