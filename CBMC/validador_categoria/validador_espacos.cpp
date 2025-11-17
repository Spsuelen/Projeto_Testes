#include <assert.h>

#define MAX_LEN 31

void __CPROVER_assume(int condition);

using namespace std;

bool validate_no_spaces(const char category[MAX_LEN], int len) {
    for (int i = 0; i < len; i++) {
        assert(category[i] != ' ');
    }
    return true;
}

int main() {
    char category[MAX_LEN];
    int len;

    __CPROVER_assume(len >= 3 && len <= 30);

    validate_no_spaces(category, len);

    return 0;
}