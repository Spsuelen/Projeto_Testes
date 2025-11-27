#include <cctype>
#include <assert.h>

#define MAX_LEN_TITLE 21

void __CPROVER_assume(int condition);


bool validate_not_only_spaces(const char title[MAX_LEN_TITLE], int len) {
    bool only_spaces = true;
    for (int i = 0; i < len; i++) {
        if (!isspace(title[i])) {
            only_spaces = false;
            break;
        }
    }
    assert(!only_spaces);
    return true;
}

int main() {
    char title[MAX_LEN_TITLE];
    int len;

    __CPROVER_assume(len >= 1 && len <= 20);

    validate_not_only_spaces(title, len);

    return 0;
}