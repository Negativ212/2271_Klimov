#include <iostream>

int main() {
    {
    std::cout << reinterpret_cast <double*>(3000) - reinterpret_cast <double*>(2000) << " " << sizeof(double) << std::endl;
    }
    {
    std::cout << reinterpret_cast <int*>(3000) - reinterpret_cast <int*>(2000) << " " << sizeof(int) << std::endl;
    }
    {
    std::cout << reinterpret_cast <char*>(3000) - reinterpret_cast <char*>(2000) << " " << sizeof(char) << std::endl;
    }
    return 0;
}
