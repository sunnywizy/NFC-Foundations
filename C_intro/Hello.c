#include <stdio.h>
/**
* @file type_and_size.C
* @anchor Sunday Obasi (sundayobasi222@gmail.com)
* @brief entry function
* @version 0.1
* @date 2022-09-06
*/
int sayHi();
int add_two (int x, int y);
int max (int num1, int num2, int num3);

int main ()
{
    int x = 5, y = 6, z = 24;
    printf("%d\n", x + y + z);
    // char
    char C = '1';
    // print 'char is 1 byte'

    printf ("char is %c byte \n", C);

    sayHi("Sunday", 23);

    add_two (4, 8);

   printf("The one that is greater than will appear %d\n", max(5, 8, 10));


    return (0);
}

// Creating a function that has to deal with name and age.
int sayHi (char name[], int age)
{
    printf ("Hello %s, you are %d\n", name, age);
}

// Creating that has to deal calculating two numbers and this my assignment.
int add_two (int x, int y)
{
int result = x + y;
printf("Here is the answer %d\n", result);

return (result);
}

// Learning how to use if, else if and else statement.
int max (int num1, int num2, int num3)
{
    int result;
    if( num1 > num2 && num1 > num3)
    {
        result = num1;
    } else if (num2 > num1 && num2 > num3)
    {
       result = num2;
    } else
    {
        result = num3;
    }
    
    return (result);
}
