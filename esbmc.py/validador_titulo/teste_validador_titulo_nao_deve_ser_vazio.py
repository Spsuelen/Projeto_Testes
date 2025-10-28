MAX_LEN = 20

def validate_title_not_empty(title: str)-> None:
    assert title != "", "O título não pode ser vazio."

def main() -> None:
    title = ""
    validate_title_not_empty(title)

main()
