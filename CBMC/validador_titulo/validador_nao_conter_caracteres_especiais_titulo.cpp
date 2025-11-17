#include <cctype>
#include <assert.h>

#define MAX_LEN_TITLE 21

void __CPROVER_assume(int condition);

using namespace std;

bool validate_no_special_characters(const char title[MAX_LEN_TITLE], int len) {
    const char specials[] = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`";
    for (int i = 0; i < len; i++) {
        for (int j = 0; specials[j] != '\0'; j++) {
            assert(title[i] != specials[j]);
        }
    }
    return true;
}

int main() {
    char title[MAX_LEN_TITLE];
    int len;

    __CPROVER_assume(len >= 1 && len <= 20);

    validate_no_special_characters(title, len);

    return 0;
}