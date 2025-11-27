#include <cctype>
#include <assert.h>
#define MAX_LEN 31 
void __CPROVER_assume(int condition);
using namespace std;
bool validate_category(const char category[MAX_LEN], int len) {
    const char specials[] = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`";

    assert(len >= 3 && len <= 30);

    assert(isalpha(category[0]));

    for (int i = 0; i < len - 1; i++) {
        assert(category[i] != category[i + 1]);
    }

    for (int i = 0; i < len; i++) {
        assert(category[i] != ' ');
    }

    for (int i = 0; i < len; i++) {
        for (int j = 0; specials[j] != '\0'; j++) {
            assert(category[i] != specials[j]);
        }
    }

    char last = category[len - 1];
    for (int j = 0; specials[j] != '\0'; j++) {
        assert(last != specials[j]);
    }
    assert(!isdigit(last));

    for (int i = 0; i < len; i++) {
        assert(isalpha(category[i]));
    }

    return true;
}

int main() {
    char test[MAX_LEN];
    int len;

    __CPROVER_assume(len >= 3 && len <= 30);

    for (int i = 0; i < len; i++) {
        __CPROVER_assume(test[i] >= 32 && test[i] <= 126);
    }

    for (int i = len; i < MAX_LEN; i++) {
        test[i] = '\0';
    }

    validate_category(test, len);

    return 0;
}