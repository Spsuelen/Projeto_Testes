#include <cctype>

#define MAX_LEN 31

using namespace std;

bool validate_start_with_letter(const char category[MAX_LEN]) {
    __ESBMC_assert(isalpha(category[0]), "A categoria deve começar com uma letra.");
    return true;
}

int main() {
    char category[MAX_LEN];
    int len;

    __ESBMC_assume(len >= 3 && len <= 30);
    __ESBMC_assume(category[0] >= 32 && category[0] <= 126);

    validate_start_with_letter(category);

    return 0;
}
