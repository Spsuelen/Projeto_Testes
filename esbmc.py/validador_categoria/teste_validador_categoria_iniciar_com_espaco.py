MAX_LEN = 30

def validate_category(category: str):
    assert category[0] != ' ', "A categoria não pode começar com espaço."

def main() -> None:
    category = "  Livros"
    validate_category(category)

main()
