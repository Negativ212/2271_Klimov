
#include <iostream>

int main() {
    {
        int a[10];
        std::cout << &a[8] - &a[3] << std::endl;       // 5
    }
    {
        char a[10];
        std::cout << &a[8] - &a[3] << std::endl;       // 5
    }
    {
        double a[10];
        std::cout << &a[8] - &a[3] << std::endl;       // 5
    }
    return 0;
}
