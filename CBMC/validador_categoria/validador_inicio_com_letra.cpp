#include <cctype>
#include <assert.h>

#define MAX_LEN 31

void __CPROVER_assume(int condition);

using namespace std;

bool validate_start_with_letter(const char category[MAX_LEN]) {
    assert(isalpha(category[0]));
    return true;
}

int main() {
    char category[MAX_LEN];
    int len;

    __CPROVER_assume(len >= 3 && len <= 30);
    __CPROVER_assume(category[0] >= 32 && category[0] <= 126);

    validate_start_with_letter(category);

    return 0;
}