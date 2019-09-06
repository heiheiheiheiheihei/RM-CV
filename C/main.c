#include "stdio.h"
#include "windows.h"
#include "time.h"

void main(void)
{
	unsigned long FeNl[40], count = 1;
	double timeStamp;
	clock_t checkPoint = clock();

	FeNl[0] = FeNl[1] = 1;
	printf("1: 1\n2: 1\n");
	while (++count < 40)
	{
		FeNl[count] = FeNl[count - 1] + FeNl[count - 2];
		printf("%d: %d\n", count + 1, FeNl[count]);
	}
	timeStamp = (double)(clock() - checkPoint) / CLOCKS_PER_SEC;
	printf("\n ¡¤ ÔËËãºÄÊ±£º%.3fÃë\n", timeStamp);
	system("Pause");
}