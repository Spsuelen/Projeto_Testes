#include <cctype>
#include <cstdlib>

#define MAX_LEN 31

using namespace std;

bool validate_only_letters(const char category[MAX_LEN], int len) {
    for (int i = 0; i < len; i++) {
        __ESBMC_assert(isalpha(category[i]), "A categoria deve conter apenas letras (sem números).");
    }
    return true;
}

int main() {
    char category[MAX_LEN];
    int len;

    __ESBMC_assume(len >= 3 && len <= 30);

    validate_only_letters(category, len);

    return 0;
}
