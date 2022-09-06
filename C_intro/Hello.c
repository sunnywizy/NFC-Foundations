#include <stdio.h>
/**
* #main - Entry Point
*
* @return
*/

int main ()
{
    int Num1;
    int Num2;

    printf ("Enter Your First Number: ");
    scanf ("%d", &Num1);
    printf ("Enter Your Second Number: ");
    scanf ("%d", &Num2);
    printf("Total number %d", Num1 + Num2);
    
    return (0);
}