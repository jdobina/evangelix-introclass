//
//
#include <stdio.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[])
{
  int a, b, c, temp;

  a = atoi(argv[1]);
  b = atoi(argv[2]);
  c = atoi(argv[3]);

  if(a > b)
  {
    temp = b;
    b = a;
    a = temp;
//
  }
  if(b > c)
  {
    temp = c;
    c = b;
    b = temp;
//
  }
  if(a > b)
  {
    temp = b;
    b = a;
    a = temp;
//
  }

  printf("%d\n", ANGELIX_OUTPUT(int, b, "stdout"));

  return 0;
}
