#include <assert.h>

#define MAX_LEN_TITLE 21

void __CPROVER_assume(int condition);

bool validate_consecutive_repeated(const char title[MAX_LEN_TITLE], int len) {
    for (int i = 0; i < len - 1; i++) {
        assert(title[i] != title[i + 1]);
    }
    return true;
}

int main() {
    char title[MAX_LEN_TITLE];
    int len;

    __CPROVER_assume(len >= 1 && len <= 20);

    validate_consecutive_repeated(title, len);

    return 0;
}