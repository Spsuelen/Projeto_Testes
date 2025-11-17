class ValidadorCategory:
    @staticmethod
    def validate_category(category):
        if len(category) < 3 or len(category) > 30:
            return False

        if not category[0].isalpha():
            return False

        for i in range(len(category) - 1):
            if category[i] == category[i + 1]:
                return False

        caracteres_especiais_invalidos = '!@#$%^&*()_+=-[]{}|;:,.<>?/~`'

        if ' ' in category:
            return False

        if any(c in caracteres_especiais_invalidos for c in category):
            return False

        caracteres_finais_invalidos = '0123456789!@#$%^&*()_+=-[]{}|;:,.<>?/~`'
        if category[-1] in caracteres_finais_invalidos:
            return False

        if not category.isalpha():
            return False

        return True
