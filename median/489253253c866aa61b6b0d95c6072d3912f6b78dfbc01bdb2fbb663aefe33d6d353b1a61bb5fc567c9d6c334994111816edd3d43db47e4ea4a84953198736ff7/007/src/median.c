/**/

#include <stdio.h>


#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]) {
	int A, B, C, small, large, median;
	
	A = atoi(argv[1]);
	B = atoi(argv[2]);
	C = atoi(argv[3]);
	
	if (A > B){
		small = B;
		large = A;
	}
	else if (A < B) {
		small = A;
		large = B;
	}
	
	
	if (C > large) 
		median = large;
	else if (C < small)
		median = small;
	else
		median = C;
		
	printf("%d\n", ANGELIX_OUTPUT(int, median, "stdout"));
	return (0);
}


