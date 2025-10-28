#include <cctype>

#define MAX_LEN 31

using namespace std;

bool validate_no_end_special_or_digit(const char category[MAX_LEN], int len) {
    const char specials[] = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`";
    char last = category[len - 1];
    for (int j = 0; specials[j] != '\0'; j++) {
        __ESBMC_assert(last != specials[j], "A categoria não pode terminar com um número ou caractere especial.");
    }
    __ESBMC_assert(!isdigit(last), "A categoria não pode terminar com um número ou caractere especial.");
    return true;
}

int main() {
    char category[MAX_LEN];
    int len;

    __ESBMC_assume(len >= 3 && len <= 30);

    validate_no_end_special_or_digit(category, len);

    return 0;
}
