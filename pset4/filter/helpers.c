#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int avg = 0;

    // For iterating all rows and colums
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE temp = image[i][j];
            avg = round((temp.rgbtBlue + temp.rgbtGreen + temp.rgbtRed) / 3.0);
            avg = avg < 0x00 ? 0x00 : avg;
            avg = avg > 0xff ? 0xff : avg;
            temp.rgbtBlue = avg;
            temp.rgbtGreen = avg;
            temp.rgbtRed = avg;
            image[i][j] = temp;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // For iterating all rows and colums
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, k = width - 1; j < k; j++, k--)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][k];
            image[i][k] = temp;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE new_image[height][width];
    // For iterating all rows and colums
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE temp = image[i][j];
            int blurRed = temp.rgbtRed, blurGreen = temp.rgbtGreen, blurBlue = temp.rgbtBlue, count = 1;
            // left column
            if (j - 1 >= 0)
            {
                blurRed += image[i][j - 1].rgbtRed;
                blurGreen += image[i][j - 1].rgbtGreen;
                blurBlue += image[i][j - 1].rgbtBlue;
                count++;
            }
            // right column
            if (j + 1 < width)
            {
                blurRed += image[i][j + 1].rgbtRed;
                blurGreen += image[i][j + 1].rgbtGreen;
                blurBlue += image[i][j + 1].rgbtBlue;
                count++;
            }
            // upper row
            if (i - 1 >= 0)
            {
                blurRed += image[i - 1][j].rgbtRed;
                blurGreen += image[i - 1][j].rgbtGreen;
                blurBlue += image[i - 1][j].rgbtBlue;
                count++;
                // left column
                if (j - 1 >= 0)
                {
                    blurRed += image[i - 1][j - 1].rgbtRed;
                    blurGreen += image[i - 1][j - 1].rgbtGreen;
                    blurBlue += image[i - 1][j - 1].rgbtBlue;
                    count++;
                }
                // right column
                if (j + 1 < width)
                {
                    blurRed += image[i - 1][j + 1].rgbtRed;
                    blurGreen += image[i - 1][j + 1].rgbtGreen;
                    blurBlue += image[i - 1][j + 1].rgbtBlue;
                    count++;
                }
            }
            // lower row
            if (i + 1 < height)
            {
                blurRed += image[i + 1][j].rgbtRed;
                blurGreen += image[i + 1][j].rgbtGreen;
                blurBlue += image[i + 1][j].rgbtBlue;
                count++;
                // left column
                if (j - 1 >= 0)
                {
                    blurRed += image[i + 1][j - 1].rgbtRed;
                    blurGreen += image[i + 1][j - 1].rgbtGreen;
                    blurBlue += image[i + 1][j - 1].rgbtBlue;
                    count++;
                }
                // right column
                if (j + 1 < width)
                {
                    blurRed += image[i + 1][j + 1].rgbtRed;
                    blurGreen += image[i + 1][j + 1].rgbtGreen;
                    blurBlue += image[i + 1][j + 1].rgbtBlue;
                    count++;
                }
            }
            // Find average
            blurRed = round((double)blurRed / count);
            blurGreen = round((double)blurGreen / count);
            blurBlue = round((double)blurBlue / count);
            temp.rgbtRed = blurRed;
            temp.rgbtGreen = blurGreen;
            temp.rgbtBlue = blurBlue;
            new_image[i][j] = temp;
        }
    }

    // Copying array
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_image[i][j];
        }
    }

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE new_image[height][width];
    // For iterating all rows and colums
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int GxRed = 0, GxGreen = 0, GxBlue = 0;
            int GyRed = 0, GyGreen = 0, GyBlue = 0;
            // left column
            if (j - 1 >= 0)
            {
                GxRed += -2 * image[i][j - 1].rgbtRed;
                GxGreen += -2 * image[i][j - 1].rgbtGreen;
                GxBlue += -2 * image[i][j - 1].rgbtBlue;

                GyRed += 0 * image[i][j - 1].rgbtRed;
                GyGreen += 0 * image[i][j - 1].rgbtGreen;
                GyBlue += 0 * image[i][j - 1].rgbtBlue;
            }
            // right column
            if (j + 1 < width)
            {
                GxRed += 2 * image[i][j + 1].rgbtRed;
                GxGreen += 2 * image[i][j + 1].rgbtGreen;
                GxBlue += 2 * image[i][j + 1].rgbtBlue;

                GyRed += 0 * image[i][j + 1].rgbtRed;
                GyGreen += 0 * image[i][j + 1].rgbtGreen;
                GyBlue += 0 * image[i][j + 1].rgbtBlue;
            }
            // upper row
            if (i - 1 >= 0)
            {
                GxRed += 0 * image[i - 1][j].rgbtRed;
                GxGreen += 0 * image[i - 1][j].rgbtGreen;
                GxBlue += 0 * image[i - 1][j].rgbtBlue;

                GyRed += -2 * image[i - 1][j].rgbtRed;
                GyGreen += -2 * image[i - 1][j].rgbtGreen;
                GyBlue += -2 * image[i - 1][j].rgbtBlue;

                // left column
                if (j - 1 >= 0)
                {
                    GxRed += -1 * image[i - 1][j - 1].rgbtRed;
                    GxGreen += -1 * image[i - 1][j - 1].rgbtGreen;
                    GxBlue += -1 * image[i - 1][j - 1].rgbtBlue;

                    GyRed += -1 * image[i - 1][j - 1].rgbtRed;
                    GyGreen += -1 * image[i - 1][j - 1].rgbtGreen;
                    GyBlue += -1 * image[i - 1][j - 1].rgbtBlue;
                }
                // right column
                if (j + 1 < width)
                {
                    GxRed += 1 * image[i - 1][j + 1].rgbtRed;
                    GxGreen += 1 * image[i - 1][j + 1].rgbtGreen;
                    GxBlue += 1 * image[i - 1][j + 1].rgbtBlue;

                    GyRed += -1 * image[i - 1][j + 1].rgbtRed;
                    GyGreen += -1 * image[i - 1][j + 1].rgbtGreen;
                    GyBlue += -1 * image[i - 1][j + 1].rgbtBlue;
                }
            }
            // lower row
            if (i + 1 < height)
            {
                GxRed += 0 * image[i + 1][j].rgbtRed;
                GxGreen += 0 * image[i + 1][j].rgbtGreen;
                GxBlue += 0 * image[i + 1][j].rgbtBlue;

                GyRed += 2 * image[i + 1][j].rgbtRed;
                GyGreen += 2 * image[i + 1][j].rgbtGreen;
                GyBlue += 2 * image[i + 1][j].rgbtBlue;

                // left column
                if (j - 1 >= 0)
                {
                    GxRed += -1 * image[i + 1][j - 1].rgbtRed;
                    GxGreen += -1 * image[i + 1][j - 1].rgbtGreen;
                    GxBlue += -1 * image[i + 1][j - 1].rgbtBlue;

                    GyRed += 1 * image[i + 1][j - 1].rgbtRed;
                    GyGreen += 1 * image[i + 1][j - 1].rgbtGreen;
                    GyBlue += 1 * image[i + 1][j - 1].rgbtBlue;
                }
                // right column
                if (j + 1 < width)
                {
                    GxRed += 1 * image[i + 1][j + 1].rgbtRed;
                    GxGreen += 1 * image[i + 1][j + 1].rgbtGreen;
                    GxBlue += 1 * image[i + 1][j + 1].rgbtBlue;

                    GyRed += 1 * image[i + 1][j + 1].rgbtRed;
                    GyGreen += 1 * image[i + 1][j + 1].rgbtGreen;
                    GyBlue += 1 * image[i + 1][j + 1].rgbtBlue;
                }
            }

            // Find average
            long long int x = round(sqrt(GxRed * GxRed + GyRed * GyRed));
            x = x > 0xff ? 0xff : x;
            new_image[i][j].rgbtRed = x;
            x = round(sqrt(GxGreen * GxGreen + GyGreen * GyGreen));
            x = x > 0xff ? 0xff : x;
            new_image[i][j].rgbtGreen = x;
            x = round(sqrt(GxBlue * GxBlue + GyBlue * GyBlue));
            x = x > 0xff ? 0xff : x;
            new_image[i][j].rgbtBlue = x;

        }
    }

    // Copying array
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_image[i][j];
        }
    }

    return;
}
