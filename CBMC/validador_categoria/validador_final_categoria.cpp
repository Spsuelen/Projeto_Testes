#include <cctype>
#include <assert.h>

#define MAX_LEN 31

void __CPROVER_assume(int condition);

using namespace std;

bool validate_no_end_special_or_digit(const char category[MAX_LEN], int len) {
    const char specials[] = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`";
    char last = category[len - 1];
    for (int j = 0; specials[j] != '\0'; j++) {
        assert(last != specials[j]);
    }
    assert(!isdigit(last));
    return true;
}

int main() {
    char category[MAX_LEN];
    int len;

    __CPROVER_assume(len >= 3 && len <= 30);

    validate_no_end_special_or_digit(category, len);

    return 0;
}