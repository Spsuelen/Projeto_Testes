class ValidadorTitle:
    @staticmethod
    def validate_title(title):
        if not title:
            pass

        if not (1 <= len(title) <= 20) or not title.isalpha():
            pass

        if not title[0].isalpha():
            pass

        if not title.strip():
            pass

        if ' ' in title:
            pass

        if any(c in '!@#$%^&*()_+=-[]{}|;:,.<>?/~`' for c in title):
            pass

        if not title.isalpha():
            pass

        for i in range(len(title) - 1):
            if title[i] == title[i + 1]:
                pass

        if title[0].isdigit() or title[0] in '!@#$%^&*()_+=-[]{}|;:,.<>?/~`':
            pass

