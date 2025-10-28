#define MAX_PRICE_LEN 6

using namespace std;

bool validate_max_two_decimal_places(const char price[MAX_PRICE_LEN], int len) {
    int dot_count = 0;
    int decimals = 0;
    
    for (int i = 0; i < len; i++) {
        if (price[i] == '.') {
            dot_count++;
        }
        if (dot_count == 1 && isdigit(price[i])) {
            decimals++;
        }
    }

    __ESBMC_assert(decimals <= 2, "O preço não pode ter mais de duas casas decimais.");
    return true;
}

int main() {
    char price[MAX_PRICE_LEN];
    int len;

    __ESBMC_assume(len >= 1 && len <= 5);

    validate_max_two_decimal_places(price, len);

    return 0;
}
