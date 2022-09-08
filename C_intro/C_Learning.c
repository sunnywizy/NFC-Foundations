#include <stdio.h>

int main ()
{
    // Learning how to create advance calculator

    int num1;
    int num2;
    int op;

    printf("Enter your First Number: ");
    scanf("%d\n", &num1);
    printf("'Enter your operator: ");
    scanf(" %lc\n", &op);
    printf("Enter your Second Number: ");
    scanf("%d\n", &num2);

    if(op == '+')
    {
        printf("%d\n", num1 + num2);
    }else if (op == '-')
    {
        printf("%d\n", num1 - num2);
    }else if (op == '*')
    {
        printf("%d\n", num1 * num2);
    }else if (op == '/')
    {
        printf("%d\n", num1 / num2);
    }else {
        printf("Invalid Operator\n");
    }
}