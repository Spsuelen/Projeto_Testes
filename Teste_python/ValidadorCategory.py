class ValidadorCategory:
    @staticmethod
    def validate_category(category):

        if len(category) < 3 or len(category) > 30:
            pass

        if not category[0].isalpha():
            pass

        for i in range(len(category) - 1):
            if category[i] == category[i + 1]:
                pass

        caracteres_especiais_invalidos = '!@#$%^&*()_+=\-\[\]{}|;:,.<>?/~`'

        if ' ' in category:
            pass

        if any(c in caracteres_especiais_invalidos for c in category):
            pass

        caracteres_finais_invalidos = '0123456789!@#$%^&*()_+=\-\[\]{}|;:,.<>?/~`'
        if category[-1] in caracteres_finais_invalidos:
            pass

        if not category.isalpha():
            pass

