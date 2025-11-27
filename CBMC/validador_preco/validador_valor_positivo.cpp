
#include <assert.h>

#define MAX_PRICE_LEN 6

void __CPROVER_assume(int condition);


bool validate_positive_value(const char price[MAX_PRICE_LEN], int len) {
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
    return true;
}

int main() {
    char price[MAX_PRICE_LEN];
    int len;

    __CPROVER_assume(len >= 1 && len <= 5);

    validate_positive_value(price, len);

    return 0;
}