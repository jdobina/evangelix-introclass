/**/
#include <stdio.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]) {
	int a, b, c, m;
	a = atoi(argv[1]);
	b = atoi(argv[2]);
	c = atoi(argv[3]);
	if ((a>=b && a<=c) || (a>=c && a<=b))
		m = b;
	else if ((b>=a && b<=c) || (b>=c && b<=a))
		m = b;
	else 
		m = c;
		
	printf("%d\n", ANGELIX_OUTPUT(int, m, "stdout"));
	return 0;
}