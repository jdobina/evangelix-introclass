/**/

#include<stdio.h>
#include<math.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]) {

  int a,b,c,temp1,temp2;
  a = atoi(argv[1]);
  b = atoi(argv[2]);
  c = atoi(argv[3]);

  temp1=a;
  temp2=b;

  if (a>c)
    {
    a=b;
    b=temp1;
    }

  if (b>c)
    {
    b=c;
    c=temp2;
    }
  
  
  if (a>b)
    {
    a=b;
    b=temp1;
    }

  printf("%d\n", ANGELIX_OUTPUT(int, b, "stdout"));

  return 0;
  }
