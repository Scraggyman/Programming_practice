#include <iostream>

int sum_of_multiples(int n, int k) {
    int p = (n - 1) / k;
    return k * p * (p + 1) / 2;
}

int main() {
    int n = 1000;

    int total = sum_of_multiples(n, 3)
              + sum_of_multiples(n, 5)
              - sum_of_multiples(n, 15);

    std::cout << "Сумма чисел от 0 до" << n << ", кратных 3 и 5:" << total << std::endl;
    return 0;
}