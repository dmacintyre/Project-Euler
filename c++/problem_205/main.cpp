#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

int randomNum(int topVal)
{
    return (rand() % topVal + 1);
}

int rollPeter()
{
    int sum = 0;
    for (int i = 0; i < 9; i++)
    {
        sum += randomNum(4);
    }
    return sum;
}

int rollColin()
{
    int sum = 0;
    for (int i = 0; i < 6; i++)
    {
        sum += randomNum(6);
    }
    return sum;
}

int main()
{
    srand(time(NULL));
    int c_vic = 0;
    int turn = 0;
    for (int i = 0; i < 100000000; i++)
    {
        int pete_score = rollPeter();
        int colin_score = rollColin();
        if (pete_score > colin_score)
        {
            c_vic += 1;
        }
        turn += 1;
    }
    float c_vic_f = c_vic;
    float turn_f = turn;
    cout << c_vic_f/turn_f;
    return 0;
}
