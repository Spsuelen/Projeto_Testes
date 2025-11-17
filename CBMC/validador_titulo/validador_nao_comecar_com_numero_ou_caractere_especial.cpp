#include <cctype>
#include <assert.h>

#define MAX_LEN_TITLE 21

using namespace std;

bool validate_no_start_with_number_or_special(const char title[MAX_LEN_TITLE]) {
    const char specials[] = "!@#$%^&*()_+=-[]{}|;:,.<>?/~`";
    assert(!isdigit(title[0]));
    for (int j = 0; specials[j] != '\0'; j++) {
        assert(title[0] != specials[j]);
    }
    return true;
}

int main() {
    char title[MAX_LEN_TITLE];

    validate_no_start_with_number_or_special(title);

    return 0;
}