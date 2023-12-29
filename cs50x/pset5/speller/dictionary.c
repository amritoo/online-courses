// Implements a dictionary's functionality

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 143091;

// Hash table
node *table[N];

// Total loaded word count
unsigned int word_count = 0;


// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int pos = hash(word);
    node *it = table[pos];

    // Checking through the linked list
    while(it != NULL)
    {
        if (strcasecmp(it->word, word) == 0) {
            return true;
        }
        it = it->next;
    }

    return false;
}

// Hashes word to a number
// This function uses djb2 hashing algorithm first reported by dan bernstein.
// It was found from here: http://www.cse.yorku.ca/~oz/hash.html
unsigned int hash(const char *word)
{
    unsigned int hash_number = 5381;
    int c;

    // generating hash using each character in word
    while ((c = tolower(*word++)))
    {
        hash_number = ((hash_number << 5) + hash_number) + c;    /* hash * 33 + c */
    }

    return hash_number % N;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Open input file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", dictionary);
        return false;
    }

    // Prepare to load word
    int index = 0, words = 0;
    char word[LENGTH + 1];

    // load each word in dictionary
    while (fscanf(file, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fprintf(stderr, "Could not open allocate memory\n");
            return false;
        }

        int pos = hash(word);
        strcpy(n->word, word);
        n->next = table[pos];

        table[pos] = n;
        word_count++;
    }


    // Check whether there was an error
    if (ferror(file))
    {
        fclose(file);
        printf("Error reading %s.\n", dictionary);
        unload();
        return false;
    }

    // Close dictionary
    fclose(file);

    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // returning total word count
    return word_count;
}

// Unloads  dictionary from memory, returning true if successful else false
bool unload(void)
{
    // free each row of table
    for (int i = 0; i < N; i++)
    {
        node *cur = table[i], *temp;

        // frees each column of table
        while (cur != NULL)
        {
            temp = cur;
            cur = cur->next;
            free(temp);
        }
    }
    return true;
}
