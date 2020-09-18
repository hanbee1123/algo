#include <stdio.h>

int main(){
	int max = 100;
	int i;
	for(i=1; i<=max; i++){
		if (i % 15 == 0){
			printf("%s\n","FizzBuzz");
		}
		else if(i % 5 == 0) {
			printf("%s\n","Buzz");
		}
		else if(i%3 == 0){
			printf("%s\n","Fizz");
		}
        else{
            printf("%d\n", i);
        }
	}
	return 0;
}