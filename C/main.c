#include<stdio.h>
#define STUD_N    40
#define  COURSE_N  3
void AverforStd(int score[][COURSE_N],int sum[],float avar[],int n);
void AverforStd(int score[][COURSE_N],int sum[],float avar[],int n);
int main()
{int score[STUD_N][COURSE_N],sumS[STUD_N],sumC[COURSE_N],n;    
long m=num[STUD_N]
float averS[STUD_N],averC[COURSE_N]
printf("input the total number of the students(n<=40):")
scanf("%d,&n")
ReadScore(score,num,n)
{
    int i,j;
	for(i=0;i<n;i++)
	{
		sum[i]=0;
		for(j=0;j<COURSE_N;j++)
		{
			sum[i]+sum[i]+score[i][j];
		}
		avar[i]=(float)sum[i]/COURSE_N;
	}
}
int main()
{
	float x,amax,amin;
	scanf("%f",&x);
	amax=x;
	amin=x;
	while(x>=0)
	{
		if(x>amax)
		amax=x;
		if(x<amin)
		amin=x;
		scanf("%f",&x);
	}
	printf("\namax=%f\namin=%f\n",amax,amin);
	scanf("%f",&x);
	return 0;
}
