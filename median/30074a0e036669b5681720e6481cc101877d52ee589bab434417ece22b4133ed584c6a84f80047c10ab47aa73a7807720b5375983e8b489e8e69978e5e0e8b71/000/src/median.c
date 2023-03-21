/**/

#include <stdio.h>
#include <math.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]) {

int a;
int b;
int c;

a = atoi(argv[1]);
b = atoi(argv[2]);
c = atoi(argv[3]);

if( (a<b && b<c) || (b<a && c<b))
printf("%d\n", ANGELIX_OUTPUT(int, b, "stdout"));
if( (b<a && a<c) || (a<b && c<a))
printf("%d\n", ANGELIX_OUTPUT(int, a, "stdout"));
if((a<c && c<b) || (b<c && c<a))
printf("%d\n", ANGELIX_OUTPUT(int, c, "stdout"));

return 0;

}
