#include <iostream>

int main() {

    {
        int x = 1, y = 2;
        int *p = &y, *q = &x;
        
        if (p < q)
            std::cout << "Yes";
        else
            std::cout << "No";
            
    }

    {
    int y = 2, x = 1;
    int *p = &y, *q = &x;
        
    if (p < q)
        std::cout << "Yes";
    else
        std::cout << "No";
            
    }

    return 0;
}
