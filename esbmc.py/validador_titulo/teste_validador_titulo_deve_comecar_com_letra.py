MAX_LEN = 20
def validate_title(title: str):
    assert title[0].isalpha(), "O título deve começar com uma letra."

def main() -> None:
    title = "Livro"
    validate_title(title)

main()
