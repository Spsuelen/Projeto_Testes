def validate_category(category: str):
    for i in range(len(category) - 1):
        assert category[i] != category[i + 1]

def main() -> None:
    category = "Livross"
    validate_category(category)

main()
