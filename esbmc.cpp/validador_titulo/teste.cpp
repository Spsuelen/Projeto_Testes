#include <cctype>
#include <cstdlib>
#include <cstring>

#define MAX_LEN_TITLE 21 

using namespace std;

bool validate_title(const char title[MAX_LEN_TITLE], int len) {
    const char specials[] = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`";

    __ESBMC_assert(len > 0, "O campo não deve estar vazio.");

    __ESBMC_assert(len >= 1 && len <= 20, "Tamanho ou caracteres inválidos.");

    __ESBMC_assert(isalpha(title[0]), "O título deve começar com uma letra.");

    bool only_spaces = true;
    for (int i = 0; i < len; i++) {
        if (!isspace(title[i])) {
            only_spaces = false;
            break;
        }
    }
    __ESBMC_assert(!only_spaces, "O título não pode ser apenas espaços.");

    for (int i = 0; i < len; i++) {
        __ESBMC_assert(title[i] != ' ', "O título não deve conter espaços.");
    }

    for (int i = 0; i < len; i++) {
        for (int j = 0; specials[j] != '\0'; j++) {
            __ESBMC_assert(title[i] != specials[j], "O título não deve conter caracteres especiais.");
        }
    }

    for (int i = 0; i < len; i++) {
        __ESBMC_assert(isalpha(title[i]), "O título deve conter apenas letras.");
    }

    for (int i = 0; i < len - 1; i++) {
        __ESBMC_assert(title[i] != title[i + 1], "O título não deve conter caracteres repetidos consecutivos.");
    }

    __ESBMC_assert(!isdigit(title[0]), "O título não pode começar com um número ou caractere especial.");
    for (int j = 0; specials[j] != '\0'; j++) {
        __ESBMC_assert(title[0] != specials[j], "O título não pode começar com um número ou caractere especial.");
    }

    return true;
}

int main() {
    char test[MAX_LEN_TITLE];
    int len;

    __ESBMC_assume(len >= 1 && len <= 20);

    for (int i = 0; i < len; i++) {
        __ESBMC_assume(test[i] >= 32 && test[i] <= 126);
    }

    for (int i = len; i < MAX_LEN_TITLE; i++) {
        test[i] = '\0';
    }

    validate_title(test, len);

    return 0;
}
