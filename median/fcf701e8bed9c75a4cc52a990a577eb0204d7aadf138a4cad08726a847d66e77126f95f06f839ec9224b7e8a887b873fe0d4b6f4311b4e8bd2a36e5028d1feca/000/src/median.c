//
#include <stdio.h>
#include <math.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]) {

	int a, b, c;
     a = atoi(argv[1]);
     b = atoi(argv[2]);
     c = atoi(argv[3]);

	while (a<b && a<c){
		if (b<c){
		printf("%d\n", ANGELIX_OUTPUT(int, b, "stdout"));
		break;
		}
		else{
		printf("%d\n", ANGELIX_OUTPUT(int, c, "stdout"));
		break;
		}
	}

	while (b<a && b<c){
		if (a<c){
		printf("%d\n", ANGELIX_OUTPUT(int, a, "stdout"));
		break;
		}
		else{
		printf("%d\n", ANGELIX_OUTPUT(int, c, "stdout"));
		break;
		}
	}
	
	while (c<a && c<b){
		if (b<a){
		printf("%d\n", ANGELIX_OUTPUT(int, b, "stdout"));
		break;
		}
		else{
		printf("%d\n", ANGELIX_OUTPUT(int, a, "stdout"));
		break;
		}
	}

return 0;
}

 
