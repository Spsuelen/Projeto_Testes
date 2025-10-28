MAX_LEN = 30

def validate_category(category: str):
    assert category[-1] != ' ', "A categoria não pode terminar com espaço."

def main() -> None:
    category = "Livros  "
    validate_category(category)

main()
