#include <cctype>
#include <assert.h>

#define MAX_LEN_TITLE 21 

void __CPROVER_assume(int condition);

using namespace std;

bool validate_title(const char title[MAX_LEN_TITLE], int len) {
    const char specials[] = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`";

    assert(len > 0);

    assert(len >= 1 && len <= 20);

    assert(isalpha(title[0]));

    bool only_spaces = true;
    for (int i = 0; i < len; i++) {
        if (!isspace(title[i])) {
            only_spaces = false;
            break;
        }
    }
    assert(!only_spaces);

    for (int i = 0; i < len; i++) {
        assert(title[i] != ' ');
    }

    for (int i = 0; i < len; i++) {
        for (int j = 0; specials[j] != '\0'; j++) {
            assert(title[i] != specials[j]);
        }
    }

    for (int i = 0; i < len; i++) {
        assert(isalpha(title[i]));
    }

    for (int i = 0; i < len - 1; i++) {
        assert(title[i] != title[i + 1]);
    }

    assert(!isdigit(title[0]));
    for (int j = 0; specials[j] != '\0'; j++) {
        assert(title[0] != specials[j]);
    }

    return true;
}

int main() {
    char test[MAX_LEN_TITLE];
    int len;

    __CPROVER_assume(len >= 1 && len <= 20);

    for (int i = 0; i < len; i++) {
        __CPROVER_assume(test[i] >= 32 && test[i] <= 126);
    }

    for (int i = len; i < MAX_LEN_TITLE; i++) {
        test[i] = '\0';
    }

    validate_title(test, len);

    return 0;
}