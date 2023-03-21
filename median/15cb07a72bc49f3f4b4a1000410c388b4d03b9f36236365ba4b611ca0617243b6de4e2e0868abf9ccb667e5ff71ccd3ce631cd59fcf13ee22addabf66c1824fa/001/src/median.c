/**/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]){

	int	frst,
		scnd,
		thrd,
		cmp1,
		cmp2,
		med;

	frst = atoi(argv[1]);
	scnd = atoi(argv[2]);
	thrd = atoi(argv[3]);

	if(frst <= scnd)
		cmp1 = frst;
	else cmp1 = scnd;
	if(scnd <= thrd)
		cmp2 = scnd;
	else cmp2 = thrd;
	if(cmp1 >= cmp2)
		med = cmp1;
	else med = cmp2;

	//printf("%d is lesser of first 2\n%d is lesser of second 2\n", cmp1, cmp2);
	printf("%d\n", ANGELIX_OUTPUT(int, med, "stdout"));
	return 0;
}
