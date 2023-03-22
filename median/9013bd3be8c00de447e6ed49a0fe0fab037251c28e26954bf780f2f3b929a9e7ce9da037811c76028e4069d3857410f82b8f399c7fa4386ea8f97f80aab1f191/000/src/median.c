/**/

#include <stdio.h>
#include <math.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[])
{
	int first, second, third;

	first = atoi(argv[1]);
	second = atoi(argv[2]);
	third = atoi(argv[3]);

	if ((first>second && first<third) || (first<second && first>third))
		printf("%d\n", ANGELIX_OUTPUT(int, first, "stdout"));
	if ((second>first && second<third) || (second<first && second>third))
		printf("%d\n", ANGELIX_OUTPUT(int, second, "stdout"));
	if ((third>first && third<second) || (third<first && third>second))
		printf("%d\n", ANGELIX_OUTPUT(int, third, "stdout"));
	return(0);
}
