/**/

#include <stdio.h>
#include <math.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]) {

	int a,b,c,d;
	a = atoi(argv[1]);
	b = atoi(argv[2]);
	c = atoi(argv[3]);

	if ((a<b && b<c) || (c<b && b<a))
		d=b;
	if ((c<a && a<b) || (b<a && a<c))
		d=a;
	if ((b<c && c<a) || (a<c && c<b))
		d=c;

	printf("%d\n", ANGELIX_OUTPUT(int, d, "stdout"));

	return 0;
}
