#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

typedef struct
{
    BYTE bfarray[512];
} JPEGBLOCK;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: recover [infile_name]\n");
        return 1;
    }

    // Remember filenames
    char *infile = argv[1];

    // Open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 1;
    }

    // Read infile's JPEGBLOCK
    JPEGBLOCK bf;

    char outfile[10];
    int outcount = 0;
    FILE *outptr = NULL;

    while (fread(&bf, sizeof(JPEGBLOCK), 1, inptr) == 1)
    {
        if (bf.bfarray[0] == 0xff && bf.bfarray[1] == 0xd8 && bf.bfarray [2] == 0xff && (bf.bfarray[3] & 0xf0) == 0xe0)
        {
            // Closes previous file if opened
            if (outptr != NULL)
            {
                fclose(outptr);
                outcount++;
            }
            sprintf(outfile, "%03d.jpg", outcount);

            // Open output file
            outptr = fopen(outfile, "w");
            if (outptr == NULL)
            {
                fprintf(stderr, "Could not create %s.\n", outfile);
                return 1;
            }

            // Write outfile's JPEGBLOCK
            fwrite(&bf, sizeof(JPEGBLOCK), 1, outptr);
        }
        else if (outptr != NULL)
        {
            // Write outfile's JPEGBLOCK
            fwrite(&bf, sizeof(JPEGBLOCK), 1, outptr);
        }
    }
    // For closing unclosed files
    fclose(inptr);
    if (outptr != NULL)
    {
        fclose(outptr);
    }

    return 0;
}
