#include <assert.h>

#define MAX_PRICE_LEN 6

void __CPROVER_assume(int condition); 

bool validate_length(int len) {
    assert(len >= 1 && len <= 5);
    return true;
}

int main() {
    int len;
    __CPROVER_assume(len >= 1 && len <= 5);

    validate_length(len);

    return 0;
}