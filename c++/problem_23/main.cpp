#include <iostream>
#include <math.h>
#include <set>

using namespace std;

set<int> factors( int num )
{
    set<int> facs;
    facs.insert(1);
    for (int i = 2; i <= sqrt(num); i++)
    {
        // Is a valid factor
        if (num % i == 0)
        {
            facs.insert(i);
            facs.insert(num/i);
        }
    }
    return facs;
}

void printSet(set<int> s)
{
    for (set<int>::iterator it = s.begin(); it != s.end(); it++)
    {
        cout << *it << endl;
    }
}

int sumOfFactors(set<int> s)
{
    unsigned int sum = 0;
    for (set<int>::iterator it = s.begin(); it != s.end(); it++)
    {
        sum += *it;
    }
    return sum;
}

bool isPerfect(int num)
{
    set<int> facs = factors(num);
    return num == sumOfFactors(facs);

}

bool isAbundant(int num)
{
    set<int> facs = factors(num);
    return num < sumOfFactors(facs);
}

bool isDeficient(int num)
{
    set<int> facs = factors(num);
    return num > sumOfFactors(facs);
}

int main()
{
    // Determine All possible abundant numbers less than 28123
    set<int> possible_abundant_numbers;
    for (int i = 12; i < 28123; i++)
    {
        if (isAbundant(i))
        {
            possible_abundant_numbers.insert(i);
        }
    }
    // Generate all possible abundant numbers
    set<int> abundant_num_sums;
    for (set<int>::iterator it1 = possible_abundant_numbers.begin(); it1 != possible_abundant_numbers.end(); it1++)
    {
        for (set<int>::iterator it2 = it1; it2 != possible_abundant_numbers.end(); it2++)
        {
            if ((*it1 + *it2) > 28124)
            {
                break;
            } else
            {
                abundant_num_sums.insert(*it1 + *it2);
            }
        }
    }
    unsigned int res = 0;
    for (int i = 1; i < 28124; i++)
    {
        // Sum up all numbers which cannot be written as two abundant numbers
        if (abundant_num_sums.find(i) == abundant_num_sums.end())
        {
            res += i;
        }
    }
    cout << res << endl;
    return 0;
}
