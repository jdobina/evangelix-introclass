/**/
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]){
int a, b, c, median;
a = atoi(argv[1]);
b = atoi(argv[2]);
c = atoi(argv[3]);
if (a > b && a < c)
	median = a;
else if (b > a && b < c)
	median = b;
else if (c > a && c < b)
	median = c;
printf("%d\n", ANGELIX_OUTPUT(int, median, "stdout"));
return 0;}