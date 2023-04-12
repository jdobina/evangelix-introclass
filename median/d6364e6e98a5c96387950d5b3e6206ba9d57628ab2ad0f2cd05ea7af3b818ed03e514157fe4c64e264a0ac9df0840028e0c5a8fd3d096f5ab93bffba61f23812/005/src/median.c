/**/
//

#include <stdio.h>

#include <stdlib.h>
#ifndef ANGELIX_OUTPUT
#define ANGELIX_OUTPUT(type, expr, id) expr
#endif
int main(int argc, char *argv[]) {
	int data[3], temp=0; //
	data[1] = atoi(argv[1]);
	data[2] = atoi(argv[2]);
	data[3] = atoi(argv[3]); //
	//
	while (!((data[1] <= data[2]) && (data[2] <= data[3]))) {//
		if(data[2] <= data[1]) {
			temp=data[2];
			data[2]=data[1];
			data[1]=temp;
		} //
		if(data[3] <= data[2]) {
			temp=data[3];
			data[3]=data[2];
			data[2]=data[3];
		} //
		//
	}
	printf("%d\n", ANGELIX_OUTPUT(int, data[2], "stdout"));
	return 0;
}

