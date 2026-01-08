#include <cctype>

#define MAX_LEN 31

using namespace std;

bool validate_no_special_characters(const char category[MAX_LEN], int len) {
    const char specials[] = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`";
    for (int i = 0; i < len; i++) {
        for (int j = 0; specials[j] != '\0'; j++) {
            __ESBMC_assert(category[i] != specials[j], "A categoria não deve conter caracteres especiais.");
        }
    }
    return true;
}

int main() {
    char category[MAX_LEN];
    int len;

    __ESBMC_assume(len >= 3 && len <= 30);

    validate_no_special_characters(category, len);

    return 0;
}
