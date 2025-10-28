#define MAX_PRICE_LEN 6

using namespace std;

bool validate_length(int len) {
    __ESBMC_assert(len >= 1 && len <= 5, "Tamanho Incorreto.");
    return true;
}

int main() {
    int len;
    __ESBMC_assume(len >= 1 && len <= 5);

    validate_length(len);

    return 0;
}
