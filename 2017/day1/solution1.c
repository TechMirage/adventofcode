#include <stdio.h>
#include <stdlib.h>
#include <string.h>

FILE *fp;
int sum = 0;

#define MAXCHAR 2100

int main (void)
{
    // Here we go to start with!

    fp = fopen("input1.txt", "r");

    // Check to make sure the file opened properly, if not, just close the program.

    if (fp == NULL) {
        printf("The file didn't open properly... try again!\n");
    } else { 
        printf("File opened successfully!\n");
    }

    char c,lastchar;
    int i;

    char s[MAXCHAR];
    fgets(s, MAXCHAR, fp);
    
    // Loop through the entire string, one character at a time.
    for(i=0;i < strlen(s); i++){

        // If the character is the same as the last character, add it to the sum (after making it into an integer)
        if (s[i] == lastchar) {
           sum = sum + (s[i] -'0');
        }

        // Update the last character before moving on.
        lastchar = s[i]; 

    }
    
    // Have to check to make sure that the wrap around is good... check the first and last characters for similarities.
    if(s[0] == s[strlen(s) - 2]) {
        sum = sum + (s[0] - '0');
    }

    // Print the sum and then call it a day!
    printf("The appropiate sum is %d.\n",sum);
    return 0;
            
} 
