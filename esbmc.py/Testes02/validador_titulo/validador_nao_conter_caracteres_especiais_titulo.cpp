#include <cctype>

#define MAX_LEN_TITLE 21

using namespace std;

bool validate_no_special_characters(const char title[MAX_LEN_TITLE], int len) {
    const char specials[] = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`";
    for (int i = 0; i < len; i++) {
        for (int j = 0; specials[j] != '\0'; j++) {
            __ESBMC_assert(title[i] != specials[j], "O título não deve conter caracteres especiais.");
        }
    }
    return true;
}

int main() {
    char title[MAX_LEN_TITLE];
    int len;

    __ESBMC_assume(len >= 1 && len <= 20);

    validate_no_special_characters(title, len);

    return 0;
}
