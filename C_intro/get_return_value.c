#include <stdio.h>
/**
* @file type_and_size.C
* @anchor Sunday Obasi (sundayobasi222@gmail.com)
* @brief entry function
* @version 0.1
* @date 2022-09-06
*/
int add_two (int x, int y);

int main ()
{
    int result = add_two(4, 8);
    printf("Answer %d\n", result);

    return (0);
}


// Creating that has to deal calculating two numbers and this my assignment.
int add_two (int x, int y)
{
    int result = x + y;
    return (result);
}


