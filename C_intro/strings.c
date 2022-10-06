#include<stdio.h>
/**
 *  @file
 *  @anchor
 *  @brief The Strings
 *  @version
 *  @date
 * 
 */

int main () {
    char firstName [50];
    char lastName [50];
    // char myName[7] = "Sunday";
    // int n = 0;

    // for (n; n <= 7;) {
    //     printf("%c", myName[n]);
    //     n = n+1;
    // }
    // putchar('\n');
    printf("what is your first name? ");
    scanf("%s", firstName);
    printf("what is your last name? ");
    scanf("%s", lastName);
    printf("Nice meeting you %s %s\n", firstName, lastName);

    return (0);
}