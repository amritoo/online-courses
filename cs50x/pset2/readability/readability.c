#include<stdio.h>
#include<cs50.h>
#include<math.h>

int main(void)
{
    //inputting text
    string text = get_string("Text: ");

    int letter = 0, word = 0, sen = 0;
    bool flag = true;

    //iterate through the string
    for (int i = 0; text[i] != '\0'; i++)
    {
        //counting letter
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            letter++;
            //counting word
            if (flag)
            {
                word++;
                flag = false;
            }
        }
        else if (text[i] == ' ')
        {
            flag = true;
        }
        ///counting sentence
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            flag = true;
            sen++;
        }
    }

    //calculating
    float L = (100.0F * letter) / word, S = (100.0F * sen) / word;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = round(index);

    //printing result
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", grade);
    }

    return 0;
}