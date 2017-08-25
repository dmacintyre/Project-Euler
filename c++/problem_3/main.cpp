#include <iostream>
#include <vector>

using namespace std;

vector<int> factors(int num) {
    vector<int> vec;
    for (int i = 1; i <= num; i++) {
        // i is a factor of num
        if (num % i == 0) {
            vec.push_back(i);
        }
    }
    return vec;
}

bool isPrime(int num) {
    if (factors(num).size() == 2) {
        return true;
    } else {
    return false;
    }
}

int main()
{
    for (int i = 1; i < 121; i++) {
        cout << i << " : " << isPrime(i) << endl;
    }
    return 0;
}
