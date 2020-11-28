#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{

    /* Declare initial variables and prepare to open the file. */
    FILE* input = fopen("input1.txt", "r");
    char line[2048];
    int sum = 0;

    /* Loop through each line of the file, so that we can look at things there individually. */
    while (fgets(line,sizeof(line),input)) 
    {
        /* Read line by line and split the individual elements up into seperate pieces. */
        char *token;
        const char delim[2] = " \t";
        char *rest = line;
        
        /* Initialize our comparison variables from this data. */
        int lineMax,lineMin;
        int j = 0; /* Counter to make sure that we know where the first token is in the next while loop. */

        /* Loop through each token, to compare to the now set lineMax/lineMin. */
        while(( token = strtok_r(rest, delim, &rest))) 
        {
            /* If it's the first token, then set the lineMax/lineMin. */
            if(j == 0) 
            {
                lineMax = atoi(token);
                lineMin = atoi(token);
            }
            /* And then increment the counter again. */
            j++;

            /* Check to see if the current token is higher or lower than the max/min. If so, reset those at this point. */
            if (atoi(token) < lineMin) 
            {
                lineMin = atoi(token);
            }
            else if (atoi(token) > lineMax)
            {
                lineMax = atoi(token);
            }
 
        }
        /* Now that we've found the max and min of the line, we should be able to add the difference to the running checksum */
        sum += (lineMax - lineMin);
    }

    /* Reclose the file, of course. */
    fclose(input);

    /* Should probably print out what the actual checksum is at some point, so it seems good to do it here. */
    printf("Answer: %d\n", sum);
    return 0;


}
