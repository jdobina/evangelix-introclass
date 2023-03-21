#include <stdio.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[])

{
  int i1, i2, i3;
  i1 = atoi(argv[1]);
  i2 = atoi(argv[2]);
  i3 = atoi(argv[3]);
  if ((i1 >= i2 && i1 <= i3) || (i1 == i2 && i1 == i3) || (i1 > i2 && i1 < i3))
  printf("%d\n", ANGELIX_OUTPUT(int, i1, "stdout"));
  else if ((i2 >= i1 && i2 <= i3) || (i2 == i1 && i2 == i3) || (i2 > i1 && i2 < i3))
  printf("%d\n", ANGELIX_OUTPUT(int, i2, "stdout"));
  else if ((i3 >= i2 && i3 <= i1) || (i3 == i2 && i3 == i1) || (i3 > i2 && i3 < i1))
  printf("%d\n", ANGELIX_OUTPUT(int, i3, "stdout"));
  return (0);
}
