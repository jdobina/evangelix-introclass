//
//
#include <stdio.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[])
{
  int a, b, c, median;

  a = atoi(argv[1]);
  b = atoi(argv[2]);
  c = atoi(argv[3]);

  if((a >= b && a <= c) || (a >= c && a <= b))
    median = a;
  if((b >= a && b <= c) || (b >= c && b <= a))
    median = b;
  else
    median = c;

  printf("%d\n", ANGELIX_OUTPUT(int, median, "stdout"));

  return 0;
}
