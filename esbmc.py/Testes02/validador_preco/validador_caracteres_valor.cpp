#include <cctype>

#define MAX_PRICE_LEN 6

using namespace std;

bool validate_characters(const char price[MAX_PRICE_LEN], int len) {
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
    return true;
}

int main() {
    char price[MAX_PRICE_LEN];
    int len;

    __ESBMC_assume(len >= 1 && len <= 5);

    validate_characters(price, len);

    return 0;
}
