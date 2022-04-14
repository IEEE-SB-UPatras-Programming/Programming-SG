#include "stdio.h"
#include "stdlib.h"

int main(int argc, char *argv[])
{

	int* n = (int*)malloc(sizeof(int));
	char c = 'p';

	printf("Memory location: %x\n", n);

	int* a = (int*)malloc(10*sizeof(int));

	a[0] = 665;
	a[1] = 1665;
	a[2] = 1667;
	a[3] = 8888;

	while (c != 'q')
	{

		printf("What do you want to do: ");
		c = getchar();

		switch (c) 
		{
			case 'n':
				scanf("%d", n);
				break;

			case 'p':
				break;

			case 'a':
				for (int i = 0; i < 10; i++)
				{
					printf("%d ", a[i]);
				}
				printf("\n");
				break;
			default:
				break;
		}

		printf("n: %d\n", *n);
	}


	return 0;
}
