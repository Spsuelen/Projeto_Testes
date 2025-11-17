#include <cctype>
#include <assert.h>

#define MAX_PRICE_LEN 6

void __CPROVER_assume(int condition);

using namespace std;

bool validate_max_two_decimal_places(const char price[MAX_PRICE_LEN], int len) {
    int dot_count = 0;
    int decimals = 0;
    
    for (int i = 0; i < len; i++) {
        if (price[i] == '.') {
            dot_count++;
        }
        if (dot_count == 1 && isdigit(price[i])) {
            decimals++;
        }
    }

    assert(decimals <= 2);
    return true;
}

int main() {
    char price[MAX_PRICE_LEN];
    int len;

    __CPROVER_assume(len >= 1 && len <= 5);

    validate_max_two_decimal_places(price, len);

    return 0;
}