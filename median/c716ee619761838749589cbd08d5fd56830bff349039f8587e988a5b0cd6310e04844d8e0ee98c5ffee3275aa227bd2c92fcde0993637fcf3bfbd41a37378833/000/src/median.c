/**/

#include <stdio.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[])
{

	int A, B, C;
	A = atoi(argv[1]);
	B = atoi(argv[2]);
	C = atoi(argv[3]);

	if ( A > B && A < C)
		printf("%d\n", ANGELIX_OUTPUT(int, A, "stdout"));
	if ( A > C && A < B)
		printf("%d\n", ANGELIX_OUTPUT(int, A, "stdout"));
	if ( B > C && B < A)
		printf("%d\n", ANGELIX_OUTPUT(int, B, "stdout"));
	if ( B > A && B < C)
		printf("%d\n", ANGELIX_OUTPUT(int, B, "stdout"));
	if ( C > A && C < B)
		printf("%d\n", ANGELIX_OUTPUT(int, C, "stdout"));
	if ( C > B && C < A)
		printf("%d\n", ANGELIX_OUTPUT(int, C, "stdout"));

return(0);
}
