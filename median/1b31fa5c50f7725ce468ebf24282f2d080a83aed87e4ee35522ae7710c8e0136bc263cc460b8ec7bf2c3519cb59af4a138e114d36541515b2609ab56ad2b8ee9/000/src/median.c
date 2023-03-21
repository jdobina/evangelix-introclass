/**/

#include <stdio.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[])
{
	int num1, num2, num3;

	num1 = atoi(argv[1]);
	num2 = atoi(argv[2]);
	num3 = atoi(argv[3]);

	if((((num1 > num2) && (num1 < num3))) || ((num1 > num3) && (num1 < num2)))
	{
		printf("%d\n", ANGELIX_OUTPUT(int, num1, "stdout"));

		return 0;
	}

	else if((((num2 > num1) && (num2 < num3))) || ((num2 > num3) && (num2 < num1)))

        {
                printf("%d\n", ANGELIX_OUTPUT(int, num2, "stdout"));

		return 0;
        }

	else if((((num3 > num2) && (num3 < num1))) || ((num3 > num1) && (num3 < num2)))

        {
                printf("%d\n", ANGELIX_OUTPUT(int, num3, "stdout"));

		return 0;
        }

	return 0;
}
