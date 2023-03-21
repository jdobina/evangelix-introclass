/**/

#include <stdio.h>
#include <math.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[])
{

int x,y,z;

x = atoi(argv[1]);
y = atoi(argv[2]);
z = atoi(argv[3]);

if (x == y)
	printf("%d\n", ANGELIX_OUTPUT(int, x, "stdout"));

if (x == z)
	printf("%d\n", ANGELIX_OUTPUT(int, x, "stdout"));

if (y == z)
	printf("%d\n", ANGELIX_OUTPUT(int, y, "stdout"));

return(0);
}

