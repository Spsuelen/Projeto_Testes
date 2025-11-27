#include <assert.h>

#define MAX_LEN 31

void __CPROVER_assume(int condition);



bool validate_consecutive_repeated(const char category[MAX_LEN], int len) {
    for (int i = 0; i < len - 1; i++) {
        assert(category[i] != category[i + 1]);
    }
    return true;
}

int main() {
    char category[MAX_LEN];
    int len;

    __CPROVER_assume(len >= 3 && len <= 30);

    validate_consecutive_repeated(category, len);

    return 0;
}