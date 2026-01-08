#define MAX_LEN_TITLE 21

using namespace std;

bool validate_consecutive_repeated(const char title[MAX_LEN_TITLE], int len) {
    for (int i = 0; i < len - 1; i++) {
        __ESBMC_assert(title[i] != title[i + 1], "O título não deve conter caracteres repetidos consecutivos.");
    }
    return true;
}

int main() {
    char title[MAX_LEN_TITLE];
    int len;

    __ESBMC_assume(len >= 1 && len <= 20);

    validate_consecutive_repeated(title, len);

    return 0;
}
