class ValidatorExpense:
    @staticmethod
    def validate_price(price):
        if not price.replace('.', '').isdigit() or not (1 <= len(price) <= 5):
            return False

        try:
            if float(price) <= 0:
                return False
        except ValueError:
            return False

        if '.' in price and len(price.split('.')[1]) > 2:
            return False

        if not price.replace('.', '').isdigit():
            return False

        if price[0] == '.':
            return False

        if price.count('.') > 1:
            return False

        return True
