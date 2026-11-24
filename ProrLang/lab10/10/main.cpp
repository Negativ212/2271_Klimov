#include <iostream>

int main() {
    int x[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int *p = x + 5;
    int *q = &x[5];

    std::cout << "p = " << p << std::endl;
    std::cout << "q = " << q << std::endl;
    std::cout << "p == q: " << (p == q) << std::endl;   // 1
    std::cout << "*p = " << *p << std::endl;            // 6
    std::cout << "*q = " << *q << std::endl;            // 6
    std::cout << "p - x = " << p - x << std::endl;      // 5
    std::cout << "q - x = " << q - x << std::endl;      // 5

    return 0;
}