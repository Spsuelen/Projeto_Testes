#include <cstdlib>

#define MAX_LEN 31

using namespace std;

bool validate_length(int len) {
    __ESBMC_assert(len >= 3 && len <= 30, "A categoria deve ter entre 3 e 30 caracteres.");
    return true;
}

int main() {
    int len;
    __ESBMC_assume(len >= 3 && len <= 30);

    validate_length(len);

    return 0;
}
