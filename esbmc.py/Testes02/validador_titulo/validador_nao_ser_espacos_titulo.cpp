#define MAX_LEN_TITLE 21

using namespace std;

bool validate_not_only_spaces(const char title[MAX_LEN_TITLE], int len) {
    bool only_spaces = true;
    for (int i = 0; i < len; i++) {
        if (!isspace(title[i])) {
            only_spaces = false;
            break;
        }
    }
    __ESBMC_assert(!only_spaces, "O título não pode ser apenas espaços.");
    return true;
}

int main() {
    char title[MAX_LEN_TITLE];
    int len;

    __ESBMC_assume(len >= 1 && len <= 20);

    validate_not_only_spaces(title, len);

    return 0;
}
