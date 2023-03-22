/**/

#include <stdio.h>


#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]) 
{

	int n1, n2, n3;
	n1 = atoi(argv[1]);
	n2 = atoi(argv[2]);
	n3 = atoi(argv[3]);
	if ((n1>n2)&&(n1>n3)&&(n2>n3))
		printf("%d\n", ANGELIX_OUTPUT(int, n2, "stdout"));
	else if ((n1>n2)&&(n1>n3)&&(n3>n2))
		printf("%d\n", ANGELIX_OUTPUT(int, n3, "stdout"));
	else if ((n2>n1)&&(n2>n3)&&(n3>n1))
		printf("%d\n", ANGELIX_OUTPUT(int, n3, "stdout"));
	else if ((n2>n1)&&(n2>n3)&&(n1>n3))
		printf("%d\n", ANGELIX_OUTPUT(int, n1, "stdout"));
	else if ((n3>n1)&&(n3>n2)&&(n1>n2))
		printf("%d\n", ANGELIX_OUTPUT(int, n1, "stdout"));
	else if ((n3>n1)&&(n3>n2)&&(n2>n1))
		printf("%d\n", ANGELIX_OUTPUT(int, n2, "stdout"));
	return(0);
}
