MAX_PRICE_LEN: int = 6

def validate_length_price(length: int) -> bool:
    assert 1 <= length <= 5, "Tamanho Incorreto."
    return True

def validate_characters(price: str, length: int) -> bool:
    dot_count: int = 0
    i: int = 0
    while i < length:
        c: str = price[i]
        if c == '.':
            dot_count += 1
        else:
            assert c.isdigit(), "O preço deve conter apenas números e, no máximo, um ponto."
        i += 1
    assert dot_count <= 1, "O preço não pode conter mais de um ponto."
    return True

def validate_max_two_decimal_places(price: str, length: int) -> bool:
    dot_count: int = 0
    decimals: int = 0
    i: int = 0
    while i < length:
        c: str = price[i]
        if c == '.':
            dot_count += 1
        elif dot_count == 1 and c.isdigit():
            decimals += 1
        i += 1
    assert decimals <= 2, "O preço não pode ter mais de duas casas decimais."
    return True

def validate_no_start_with_dot(price: str) -> bool:
    assert price[0] != '.', "O preço não pode começar com um ponto."
    return True

def validate_positive_value(price: str, length: int) -> bool:
    value: float = 0.0
    factor: float = 1.0
    after_dot: bool = False
    i: int = 0
    while i < length:
        c: str = price[i]
        if c == '.':
            after_dot = True
            i += 1
            continue
        value = value * 10 + (ord(c) - ord('0'))
        if after_dot:
            factor *= 10
        i += 1
    value /= factor
    assert value > 0, "O preço deve ser um valor positivo."
    return True

def main() -> None:
    price: str = input()
    length_price: int = len(price)

    assert 1 <= length_price <= 5

    validate_length_price(length_price)
    validate_characters(price, length_price)
    validate_no_start_with_dot(price)
    validate_max_two_decimal_places(price, length_price)
    validate_positive_value(price, length_price)

main()