#include <cctype>
#include <assert.h>

#define MAX_PRICE_LEN 6

void __CPROVER_assume(int condition);

bool validate_price(const char price[MAX_PRICE_LEN], int len) {

    assert(len >= 1 && len <= 5);

    int dot_count = 0;

    for (int i = 0; i < len; i++) {
        char c = price[i];
        if (c == '.') {
            dot_count++;
        } else {
            assert(isdigit(c));
        }
    }

    assert(dot_count <= 1);

    assert(price[0] != '.');


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

    assert(value > 0);

    assert(decimals <= 2);

    return true;
}

int main() {
    char price[MAX_PRICE_LEN];
    int len;

    __CPROVER_assume(len >= 1 && len <= 5);

    for (int i = 0; i < len; i++) {
        __CPROVER_assume(price[i] >= 32 && price[i] <= 126);
    }
    for (int i = len; i < MAX_PRICE_LEN; i++) {
        price[i] = '\0';
    }

    validate_price(price, len);

    return 0;
}