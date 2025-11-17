class ValidadorTitle:
    @staticmethod
    def validate_title(title):
        if not title:
            return False

        if not (1 <= len(title) <= 20) or not title.isalpha():
            return False

        if not title[0].isalpha():
            return False

        if not title.strip():
            return False

        if ' ' in title:
            return False

        if any(c in '!@#$%^&*()_+=-[]{}|;:,.<>?/~`' for c in title):
            return False

        if title[0].isdigit() or title[0] in '!@#$%^&*()_+=-[]{}|;:,.<>?/~`':
            return False

        return True
