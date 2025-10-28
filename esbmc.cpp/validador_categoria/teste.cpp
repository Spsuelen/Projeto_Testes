#include <cctype>
#include <cstdlib>
#include <cstring>

#define MAX_LEN 31 

using namespace std;

bool validate_category(const char category[MAX_LEN], int len) {
    const char specials[] = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`";

    __ESBMC_assert(len >= 3 && len <= 30, "A categoria deve ter entre 3 e 30 caracteres.");

    __ESBMC_assert(isalpha(category[0]), "A categoria deve começar com uma letra.");

    for (int i = 0; i < len - 1; i++) {
        __ESBMC_assert(category[i] != category[i + 1], "A categoria não deve conter caracteres repetidos consecutivos.");
    }

    for (int i = 0; i < len; i++) {
        __ESBMC_assert(category[i] != ' ', "A categoria não deve conter espaços.");
    }

    for (int i = 0; i < len; i++) {
        for (int j = 0; specials[j] != '\0'; j++) {
            __ESBMC_assert(category[i] != specials[j], "A categoria não deve conter caracteres especiais.");
        }
    }

    char last = category[len - 1];
    for (int j = 0; specials[j] != '\0'; j++) {
        __ESBMC_assert(last != specials[j], "A categoria não pode terminar com um número ou caractere especial.");
    }
    __ESBMC_assert(!isdigit(last), "A categoria não pode terminar com um número ou caractere especial.");

    for (int i = 0; i < len; i++) {
        __ESBMC_assert(isalpha(category[i]), "A categoria deve conter apenas letras (sem números).");
    }

    return true;
}

int main() {
    char test[MAX_LEN];
    int len;

    __ESBMC_assume(len >= 3 && len <= 30);

    for (int i = 0; i < len; i++) {
        __ESBMC_assume(test[i] >= 32 && test[i] <= 126);
    }

    for (int i = len; i < MAX_LEN; i++) {
        test[i] = '\0';
    }

    validate_category(test, len);

    return 0;
}
