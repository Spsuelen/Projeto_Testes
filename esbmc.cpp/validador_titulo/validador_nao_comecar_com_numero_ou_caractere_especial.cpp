#include <cctype>

#define MAX_LEN_TITLE 21

using namespace std;

bool validate_no_start_with_number_or_special(const char title[MAX_LEN_TITLE]) {
    const char specials[] = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`";
    __ESBMC_assert(!isdigit(title[0]), "O título não pode começar com um número ou caractere especial.");
    for (int j = 0; specials[j] != '\0'; j++) {
        __ESBMC_assert(title[0] != specials[j], "O título não pode começar com um número ou caractere especial.");
    }
    return true;
}

int main() {
    char title[MAX_LEN_TITLE];

    validate_no_start_with_number_or_special(title);

    return 0;
}
