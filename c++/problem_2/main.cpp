#include <iostream>

using namespace std;

int main()
{
    int *p;
    int fib_seq[100000];
    p = fib_seq;
    int sum = 0;
    int i = 1;
    while (1) {
        if (i < 3) {
            *p = i;
        }
        else {
            *p = *(p-1) + *(p-2);
        }
        if (*p < 4000000) {
            if (*p % 2 == 0) {
                sum += *p;
            }
        }
        else {
            break;
        }
        p++;
        i++;

    }
    cout << sum << endl;

    return 0;
}
