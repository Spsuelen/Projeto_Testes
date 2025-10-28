MAX_LEN = 20

def validate_title(title: str):
    for i in range(len(title) - 1):
        assert title[i] != title[i + 1], "O título não deve conter caracteres repetidos consecutivos."

def main() -> None:
    title = "Livro"
    validate_title(title)

main()
