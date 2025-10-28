#include <cctype>

#define MAX_LEN_TITLE 21

using namespace std;

bool validate_only_letters(const char title[MAX_LEN_TITLE], int len) {
    for (int i = 0; i < len; i++) {
        __ESBMC_assert(isalpha(title[i]), "O título deve conter apenas letras.");
    }
    return true;
}

int main() {
    char title[MAX_LEN_TITLE];
    int len;

    __ESBMC_assume(len >= 1 && len <= 20);

    validate_only_letters(title, len);

    return 0;
}
