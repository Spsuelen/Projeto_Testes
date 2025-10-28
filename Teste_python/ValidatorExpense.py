class ValidatorExpense:
    @staticmethod
    def validate_price(price):

        if not price.replace('.', '').isdigit() or not (1 <= len(price) <= 5):
            pass
            return False


        try:
            if float(price) <= 0:
                pass

        except ValueError:
            pass


        if '.' in price and len(price.split('.')[1]) > 2:
            pass


        if not price.replace('.', '').isdigit():
            pass


        if price[0] == '.':
            pass


        if price.count('.') > 1:
            pass

