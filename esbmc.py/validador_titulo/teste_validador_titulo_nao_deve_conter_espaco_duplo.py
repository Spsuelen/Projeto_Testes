def validate_title(title: str):
    for i in range(len(title) - 1):
        assert not (title[i] == ' ' and title[i + 1] == ' ')

def main() -> None:
    title = "Livro  Antigo"
    validate_title(title)

main()
