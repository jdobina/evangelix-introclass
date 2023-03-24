/**/
#include <stdio.h>
#include <math.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[])

{
	int n1, n2, n3, temp;
	n1 = atoi(argv[1]);
	n2 = atoi(argv[2]);
	n3 = atoi(argv[3]);
	if(n2<n1)
	{
		temp=n2;
		n2=n1;
		n1=temp;
	}
	if((n3<n2)&&(n3>n1))
	{
		temp=n2;
		n2=n3;
		n3=temp;
	}
	printf("%d\n", ANGELIX_OUTPUT(int, n2, "stdout"));
	return 0;
}
