/**/
#include <stdio.h>


#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]) {

int n1, n2, n3, median;              //
n1 = atoi(argv[1]);
n2 = atoi(argv[2]);
n3 = atoi(argv[3]);    //
if(n1>=n2||n1>=n3)                      //
{
    if(n2>=n3 && n1>=n2)                //
    median=n2;
    else
    median=n1;                         //
}
else if(n2>=n3)                         //
median=n3;
else
median=n2;

printf("%d\n", ANGELIX_OUTPUT(int, median, "stdout"));






}
