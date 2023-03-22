/**/
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[])
{
	int int1, int2, int3; 
	int1 = atoi(argv[1]);
	int2 = atoi(argv[2]);
	int3 = atoi(argv[3]);

	if (((int1 <= int2) && (int1 >= int3)) || ((int1 <= int2) && (int1 >= int3)))
 	printf("%d\n", ANGELIX_OUTPUT(int, int1, "stdout"));
	else if ((((int2 <= int1)) && (int2 >= int3)) || ((int2 <= int3) && (int2 >= int1)))
        printf("%d\n", ANGELIX_OUTPUT(int, int2, "stdout"));
	else if (((int3 <= int1) && (int3 >= int2)) || ((int3 <= int2) && (int3 >= int1)))
        printf("%d\n", ANGELIX_OUTPUT(int, int3, "stdout"));
	return 0;
}                                             
