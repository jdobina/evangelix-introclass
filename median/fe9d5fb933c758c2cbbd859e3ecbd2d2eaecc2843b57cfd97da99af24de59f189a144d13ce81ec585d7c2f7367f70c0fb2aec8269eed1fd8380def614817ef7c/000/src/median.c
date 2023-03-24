//
//
#include<stdio.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]){
  int num1, num2, num3, median, big, small;

  num1 = atoi(argv[1]);
  num2 = atoi(argv[2]);
  num3  = atoi(argv[3]);

  if( num1 > num2 ){
    small = num2;
    big = num1;
  }
  else{
    big = num2;
    small = num2;
  }
  if( num3 > big )
    median = big;
  else if( num3 < small )
    median = small;
  else 
    median = num3;

  printf("%d\n", ANGELIX_OUTPUT(int, median , "stdout"));

  return 0;

}
