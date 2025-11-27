#include <assert.h>

#define MAX_LEN 31

void __CPROVER_assume(int condition);

bool validate_length(int len) {
    assert(len >= 3 && len <= 30);
    return true;
}

int main() {
    int len;
    __CPROVER_assume(len >= 3 && len <= 30);

    validate_length(len);

    return 0;
}