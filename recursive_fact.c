#include <stdio.h>

int recursive_fact(int x)
{
if(x == 0)
{
    return 1;
}

else
{
    return x * recursive_fact(x - 1);
}
}

int main(void)
{

int here = recursive_fact(5);
printf("The result is %d\n", here);
return 0;
}
