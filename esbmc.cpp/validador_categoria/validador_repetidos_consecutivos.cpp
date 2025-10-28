#define MAX_LEN 31

using namespace std;

bool validate_consecutive_repeated(const char category[MAX_LEN], int len) {
    for (int i = 0; i < len - 1; i++) {
        __ESBMC_assert(category[i] != category[i + 1], "A categoria não deve conter caracteres repetidos consecutivos.");
    }
    return true;
}

int main() {
    char category[MAX_LEN];
    int len;

    __ESBMC_assume(len >= 3 && len <= 30);

    validate_consecutive_repeated(category, len);

    return 0;
}
