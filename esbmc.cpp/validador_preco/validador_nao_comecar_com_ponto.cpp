
#define MAX_PRICE_LEN 6

using namespace std;

bool validate_no_start_with_dot(const char price[MAX_PRICE_LEN]) {
    __ESBMC_assert(price[0] != '.', "O preço não pode começar com um ponto.");
    return true;
}

int main() {
    char price[MAX_PRICE_LEN];

    validate_no_start_with_dot(price);

    return 0;
}
