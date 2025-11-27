#include <assert.h>

#define MAX_LEN_TITLE 21

void __CPROVER_assume(int condition);

bool validate_no_spaces(const char title[MAX_LEN_TITLE], int len) {
    for (int i = 0; i < len; i++) {
        assert(title[i] != ' ');
    }
    return true;
}

int main() {
    char title[MAX_LEN_TITLE];
    int len;

    __CPROVER_assume(len >= 1 && len <= 20);

    validate_no_spaces(title, len);

    return 0;
}