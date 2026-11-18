#include <iostream>

int main() {
    int a = 5;
    int b = 3;

    int *x = &a;          
    int y = *x;        
    int z = a * b;       

    int &x1 = a;           
    int *y1 = &b;        
    int y2 = a & b;   

    std::cout << y << " " << z << " " << x1 << " " << *y1 << " " << y2 << std::endl;
    
    return 0;
}
