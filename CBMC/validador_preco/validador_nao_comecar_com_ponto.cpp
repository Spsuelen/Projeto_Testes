#include <assert.h>

#define MAX_PRICE_LEN 6

bool validate_no_start_with_dot(const char price[MAX_PRICE_LEN]) {
    assert(price[0] != '.');
    return true;
}

int main() {
    char price[MAX_PRICE_LEN];

    validate_no_start_with_dot(price);

    return 0;
}