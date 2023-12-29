#include<stdio.h>
#include<cs50.h>

int main(void)
{
    int h;
    //taking input
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);

    //printing pyramid
    for (int i = 0; i < h; i++)
    {
        //printing left spaces
        for (int j = 0; i + j < h - 1; j++)
        {
            printf(" ");
        }

        //printinng left side
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }

        //printing space in between
        printf("  ");

        //printing right side
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }

        //printing newline
        printf("\n");
    }

    return 0;
}