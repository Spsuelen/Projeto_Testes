MAX_LEN = 30

def validate_category(category: str):
    for i in range(len(category) - 1):
        assert not (category[i] == ' ' and category[i + 1] == ' '), "A categoria não pode ter espaços duplos."

def main() -> None:
    category = "   livros    para   doacao"
    validate_category(category)

main()
