#define MAX_LEN_TITLE 21

using namespace std;

bool validate_no_spaces(const char title[MAX_LEN_TITLE], int len) {
    for (int i = 0; i < len; i++) {
        __ESBMC_assert(title[i] != ' ', "O título não deve conter espaços.");
    }
    return true;
}

int main() {
    char title[MAX_LEN_TITLE];
    int len;

    __ESBMC_assume(len >= 1 && len <= 20);

    validate_no_spaces(title, len);

    return 0;
}
