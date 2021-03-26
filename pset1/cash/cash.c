#include<stdio.h>
#include<math.h>
#include<cs50.h>

int main(void)
{
    //taking input
    float dollars;
    do
    {
        dollars = get_float("Change owed: ");
    }
    while (dollars < 0.0001);

    //converting
    int cents = round(dollars * 100);
    int cnt = 0;

    //nuber of querters
    cnt += cents / 25;
    cents %= 25;

    //nuber of dimes
    cnt += cents / 10;
    cents %= 10;

    //nuber of nickels
    cnt += cents / 5;
    cents %= 5;

    //nuber of pennys
    cnt += cents / 1;
    cents %= 1;

    printf("%i\n", cnt);

    return 0;
}