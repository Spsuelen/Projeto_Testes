MAX_LEN = 30

def validate_category(category: str):
    assert 3 <= len(category) <= MAX_LEN

def main() -> None:
    category = "umtesteparaverificarotamanhodacategoriaasertestadaeverificada"
    validate_category(category)

main()
