/**/
# include <stdio.h>
# include <math.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]){

	int a, b, c; 


	a = atoi(argv[1]);
	b = atoi(argv[2]);
	c = atoi(argv[3]);

	if ((a > b) && (b > c))

		printf("%d\n", ANGELIX_OUTPUT(int, b, "stdout"));

	if ((a > b) && (a > c))
	  {
		if (c > b)
		  {
			printf("%d\n", ANGELIX_OUTPUT(int, c, "stdout"));
		  }
	  }
	if ((b > a) && (a > c))

		printf("%d\n", ANGELIX_OUTPUT(int, a, "stdout"));

	if ((b > a) && (b > c))
	{
		if (c > a)
		{
			printf("%d\n", ANGELIX_OUTPUT(int, c, "stdout"));
		}
	}
        if ((c > a) && ( a > b))

                printf("%d\n", ANGELIX_OUTPUT(int, a, "stdout"));


        if ((c > a) && (c > b))
	{
                if (b > a)
		{
                        printf("%d\n", ANGELIX_OUTPUT(int, b, "stdout"));
		}
	}
	return(0);
}
