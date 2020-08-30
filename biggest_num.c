#include <stdio.h>

int biggest(int arr[5])
{

int biggest = arr[0];
for(int i = 0; i <= 5; i++)
{
    if(i > biggest)
    {
    	biggest = i;
    }
}
return biggest;
}



int main (void)
{

int my_arr[] = {1,2,3,4,5};
int here = biggest(my_arr);

printf("The biggest number is %d\n", here);

}
