#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>

int main(int argc, string argv[])
{
    //validating argc
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    //validating argv
    string key = argv[1];
    if (strlen(key) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    bool ar[26];
    //initializing to false
    for (int i = 0; i < 26; i++)
    {
        ar[i] = false;
    }

    //checking string
    for (int i = 0; key[i] != '\0'; i++)
    {
        if (isalpha(key[i]) == 0)
        {
            printf("Key must only contain alphabetic characters.\n");
            return 1;
        }
        else if (ar[toupper(key[i]) - 'A'])
        {
            printf("Key must not contain repeated characters.\n");
            return 1;
        }
        else
        {
            ar[toupper(key[i]) - 'A'] = true;
        }
    }

    string pt = get_string("plaintext: ");
    string ct = pt;

    //ciphering
    for (int i = 0; ct[i] != '\0'; i++)
    {
        //for uppercase
        if (ct[i] >= 'A' && ct[i] <= 'Z')
        {
            ct[i] = toupper(key[ct[i] - 'A']);
        }
        //for lowercase
        else if (ct[i] >= 'a' && ct[i] <= 'z')
        {
            ct[i] = tolower(key[ct[i] - 'a']);
        }
    }

    printf("ciphertext: %s\n", ct);

    return 0;
}
