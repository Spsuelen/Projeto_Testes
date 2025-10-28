#include <cctype>
#include <cstdlib>

#define MAX_PRICE_LEN 6

bool validate_price(const char price[MAX_PRICE_LEN], int len) {

    __ESBMC_assert(len >= 1 && len <= 5, "Tamanho Incorreto.");

    int dot_count = 0;

    for (int i = 0; i < len; i++) {
        char c = price[i];
        if (c == '.') {
            dot_count++;
        } else {
            __ESBMC_assert(isdigit(c), "O preço deve conter apenas números e, no máximo, um ponto.");
        }
    }

    __ESBMC_assert(dot_count <= 1, "O preço não pode conter mais de um ponto.");

    __ESBMC_assert(price[0] != '.', "O preço não pode começar com um ponto.");


    double value = 0;
    double factor = 1;
    bool after_dot = false;
    int decimals = 0;

    for (int i = 0; i < len; i++) {
        char c = price[i];
        if (c == '.') {
            after_dot = true;
            continue;
        }
        value = value * 10 + (c - '0');
        if (after_dot) {
            factor *= 10;
            decimals++;
        }
    }

    value /= factor;

    __ESBMC_assert(value > 0, "O preço deve ser um valor positivo.");

    __ESBMC_assert(decimals <= 2, "O preço não pode ter mais de duas casas decimais.");

    return true;
}

int main() {
    char price[MAX_PRICE_LEN];
    int len;

    __ESBMC_assume(len >= 1 && len <= 5);

    for (int i = 0; i < len; i++) {
        __ESBMC_assume(price[i] >= 32 && price[i] <= 126);
    }
    for (int i = len; i < MAX_PRICE_LEN; i++) {
        price[i] = '\0';
    }

    validate_price(price, len);

    return 0;
}
