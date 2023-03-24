/**/
#include <stdio.h>
#include <math.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[])
{

int a, b, c; //**/

a = atoi(argv[1]);
b = atoi(argv[2]);
c = atoi(argv[3]);

if ((a < b && b < c) || (c < b && b < a))
	printf("%d\n", ANGELIX_OUTPUT(int, b, "stdout"));
else if ((b < a && a < c) || (c < a && a < b))
	printf("%d\n", ANGELIX_OUTPUT(int, a, "stdout"));
else if ((a < c && c < b) || (b < c && c < a))
	printf("%d\n", ANGELIX_OUTPUT(int, c, "stdout"));

return 0;

}