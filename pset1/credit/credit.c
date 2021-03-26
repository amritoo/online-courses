#include<stdio.h>
#include<math.h>
#include<cs50.h>

int main(void)
{
    // taking input
    long number;
    do
    {
        number = get_long("Number: ");
    }
    while (number < 0);

    // convert to array
    int ar[20], len = 0;
    long x = number;
    //looping for digits
    while (x)
    {
        ar[len++] = x % 10;
        x /= 10;
    }
    
    // check length
    if (len < 13 || len > 16)
    {
        printf("INVALID\n");
        return 0;
    }
    
    // calculate validity
    int osum = 0, esum = 0;
    for (int i = 0; i < len; i++)
    {
        if (i % 2 == 0)
        {
            osum += ar[i];
        }
        else
        {
            x = ar[i] * 2;
            //looping for digits
            while (x)
            {
                esum += x % 10;
                x /= 10;
            }
        }
    }
    
    // print results
    if ((osum + esum) % 10 != 0)
    {
        printf("INVALID\n");
    }
    else if (len == 15 && ar[len - 1] == 3 && (ar[len - 2] == 4 || ar[len - 2] == 7))
    {
        printf("AMEX\n");
    }
    else if (len == 16 && ar[len - 1] == 5 && ar[len - 2] >= 1 && ar[len - 2] <= 5)
    {
        printf("MASTERCARD\n");
    }
    else if (ar[len - 1] == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }

    return 0;
}