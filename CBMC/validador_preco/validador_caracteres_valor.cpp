#include <cctype>
#include <assert.h>

#define MAX_PRICE_LEN 6

void __CPROVER_assume(int condition);

using namespace std;

bool validate_characters(const char price[MAX_PRICE_LEN], int len) {
    int dot_count = 0;
    for (int i = 0; i < len; i++) {
        char c = price[i];
        if (c == '.') {
            dot_count++;
        } else {
            assert(isdigit(c));
        }
    }
    assert(dot_count <= 1);
    return true;
}

int main() {
    char price[MAX_PRICE_LEN];
    int len;

    __CPROVER_assume(len >= 1 && len <= 5);

    validate_characters(price, len);

    return 0;
}