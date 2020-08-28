#include <stdio.h>

void swap(int *xp, int *yp)
{
	int temp = *xp;
	*xp = *yp;
	*yp = temp;
}

void selection_sort(int arr[], int n)
{
	int i, j, min_index;
	for(i = 0; i < n-1; i++)
	{
		min_index = i;

		for(j = i+1; j < n; j++)
			if (arr[j] < arr[min_index])
				min_index = j;
		swap(&arr[min_index], &arr[i]);	
	}
}

void print_array(int arr[], int size)
{
	int i;
	for(i = 0; i < size; i++ )
		printf("%d ", arr[i]);
	printf("\n");
}

int main()
{
	int arr[] = {64, 25, 12, 22, 11};
	int n = sizeof(arr)/sizeof(arr[0]);

	selection_sort(arr, n);

	print_array(arr, n);
	return 0;

}



