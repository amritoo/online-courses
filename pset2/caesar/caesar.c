#include<stdio.h>
#include<cs50.h>
#include<math.h>

int to_num(string s);

int main(int argc, string argv[])
{
    //validating argv
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    //validating string
    int k = to_num(argv[1]);
    if (k < 0)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    string pt = get_string("plaintext: ");
    string ct = pt;

    //ciphering
    for (int i = 0; ct[i] != '\0'; i++)
    {
        //for uppercase
        if (ct[i] >= 'A' && ct[i] <= 'Z')
        {
            ct[i] = (ct[i] - 'A' + k) % 26 + 'A';
        }
        //for lowercase
        else if (ct[i] >= 'a' && ct[i] <= 'z')
        {
            ct[i] = (ct[i] - 'a' + k) % 26 + 'a';
        }
    }

    printf("ciphertext: %s\n", ct);

    return 0;
}

int to_num(string s)
{
    int n = 0;
    //checking and converting to int
    for (int i = 0; s[i] != '\0'; i++)
    {
        //checkingand converting
        if (s[i] >= '0' && s[i] <= '9')
        {
            n = n * 10 + s[i] - '0';
        }
        else
        {
            return -1;
        }
    }
    return n;
}