/**/

#include<stdio.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]) {
  int a, b, c, median, temp;
  median = 0;
  temp = 0;
  a = atoi(argv[1]);
  b = atoi(argv[2]);
  c = atoi(argv[3]);

  if (a>=b) {
    temp = b;
    b = a;
    a = temp;
  }
  if (a<c)
    median = b;
  else if (b>c)
    median = a;
  else 
    median = c;

  printf("%d\n", ANGELIX_OUTPUT(int, median, "stdout"));

  return(0);

}
