#define MAX_LEN_TITLE 21

using namespace std;

bool validate_length(int len) {
    __ESBMC_assert(len >= 1 && len <= 20, "Tamanho ou caracteres inválidos.");
    return true;
}

int main() {
    int len;
    __ESBMC_assume(len >= 1 && len <= 20);

    validate_length(len);

    return 0;
}
