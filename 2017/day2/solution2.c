#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/* Declaration of the function that will be checking whether things divide or not. */
int checkDivides(char*, int);

int main(void)
{

    /* Declare initial variables and prepare to open the file. */
    FILE* input = fopen("inputtest2.txt", "r");
    char line[2048];
    int sum = 0;

    /* Loop through each line of the file, so that we can look at things there individually. */
    while (fgets(line,sizeof(line),input)) 
    {
        /* Read line by line and split the individual elements up into seperate pieces. */
        char *token;
        const char delim[2] = " \t";
        char *rest = line;

        /* Create a copy of the line so that we can iterate over it inside the checkDivides function. */
        char lineCpy[2048];
        memcpy(lineCpy, line, strlen(line) + 1);
        
        /* Loop through each token, to compare to the now set lineMax/lineMin. */
        while(( token = strtok_r(rest, delim, &rest))) 
        {
            /* Add in the appriopiate value to the sum, once found. */
            sum += checkDivides(lineCpy, atoi(token)); 
            getchar();
        }
        printf("sum current = %d\n", sum);
    }

    /* Reclose the file, of course. */
    fclose(input);

    /* Should probably print out what the actual checksum is at some point, so it seems good to do it here. */
    printf("Answer: %d\n", sum);
    return 0;


}

/* A function to see if there's anything on the line that divides the testValue evently. 
    If so, then pass back the quotient. If not, just pass back the zero. */
int checkDivides(char *lineCpy, int testValue)
{
    char *tokenCheck;
    const char delim[2] = " \t";
    int quotient = 0; // Keep track of the quotient of the division.
    char *restDivides = lineCpy;

    while(( tokenCheck = strtok_r(restDivides, delim, &restDivides)))
    {
        //DEBUG
        printf("current testValue = %d , current token = %d \n", testValue, atoi(tokenCheck));

        /* First check, to see if the two are the same number, because we ignore that one. */
        if (testValue != atoi(tokenCheck))
        {
            /* Now check to see if it's evenly divisible by checking the floor to compare. */
            if ((testValue / atoi(tokenCheck)) == floor(testValue / atoi(tokenCheck)))
            {
                /* If it is, then we should add that quotient into the tracking quotient here. */
                quotient = (int) (testValue / atoi(tokenCheck));
                printf("quotient = %d\n", quotient);
                getchar();
            }   
        }
    }
    
    /* Should be done at this point, return the quotient as calculated. */
    return quotient;
}

