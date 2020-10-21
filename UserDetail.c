#include<stdio.h> 
int main(void) 
{ 
	char string[25]; 
	printf("Enter the name:"); 
    scanf("%[^\n]*c",string); 
	 
	printf("My name is %s",string); 
	 
} 
