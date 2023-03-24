/**/

#include <stdio.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]) {

int A,B,C;
int Small, Large;
int Median;


A = atoi(argv[1]);
B = atoi(argv[2]);
C = atoi(argv[3]);

	if (A==B && A==C)
		Median = A;

	else if (A>B) 	{
		Large = A;
		Small = B;
	} else 		{
		Large = B;
		Small = A;
	}
		

	
	if (C>Large)
		Median = Large;
	else if (C<Small)
		Median = Small;
	else Median = C;

//**/
printf("%d\n", ANGELIX_OUTPUT(int, Median, "stdout"));

return (0);
}
