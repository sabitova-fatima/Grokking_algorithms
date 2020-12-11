#include <stdio.h>

int iter_fact(int x)
{
int result = 1;
for(int i = 1; i <=  x; i++)
  result *= i;
return result;
}

int main()
{
printf("The result is %d\n", iter_fact(5);
}
