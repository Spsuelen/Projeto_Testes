def validate_category(category: str):
    assert category[0].isalpha()

def main() -> None:
    category = "Livros"
    validate_category(category)

main()
