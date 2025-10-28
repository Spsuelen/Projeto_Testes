#define MAX_LEN 31

using namespace std;

bool validate_no_spaces(const char category[MAX_LEN], int len) {
    for (int i = 0; i < len; i++) {
        __ESBMC_assert(category[i] != ' ', "A categoria não deve conter espaços.");
    }
    return true;
}

int main() {
    char category[MAX_LEN];
    int len;

    __ESBMC_assume(len >= 3 && len <= 30);

    validate_no_spaces(category, len);

    return 0;
}
