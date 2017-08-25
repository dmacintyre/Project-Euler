#include <iostream>

using namespace std;

int main()
{
    // rows represent coin amounts
    // columns represent totals
    int coin_arr[9][201] = {0};
    // Initalize first col (which is coin amounts)
    coin_arr[1][0] = 1;
    coin_arr[2][0] = 2;
    coin_arr[3][0] = 5;
    coin_arr[4][0] = 10;
    coin_arr[5][0] = 20;
    coin_arr[6][0] = 50;
    coin_arr[7][0] = 100;
    coin_arr[8][0] = 200;
    // Initalize first row - which is possible totals
    for (int i = 0; i < 201; i++)
    {
        coin_arr[0][i] = i;
    }

    // Set possible ways to make all totals with a coin of only value 1
    for (int i = 1; i < 201; i++)
    {
        coin_arr[1][i] = 1;
    }

    for (int row = 2; row < 9; row++)
    {
        for (int col = 1; col < 201; col++)
        {
            int coin_val = coin_arr[row][0];
            int total = coin_arr[0][col];
            if (coin_val > total)
            {
                coin_arr[row][col] = coin_arr[row-1][col];
            } else if (coin_val == total)
            {
                coin_arr[row][col] = coin_arr[row-1][col] + 1;
            } else
            {
                coin_arr[row][col] = coin_arr[row-1][col] + coin_arr[row][total-coin_val];
            }
        }
    }
    cout << coin_arr[8][200] << endl;
    return 0;
}
