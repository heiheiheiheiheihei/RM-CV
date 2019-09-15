#include<stdio.h>
unsigned long Fact(unsigned int n);
int main()
{
	int m,k;
	unsigned long p;
	do{
		printf("Input m,k (m>=k>0):");
		scanf("%d,%d",&m,&k);
	}while(m<k||m<=0||k<0);
	p=Fact(m)/(Fact(k)*Fact(m-k));
	printf("p=%lu\n",p);
	scanf("%d",&m);
	return 0;
}
unsigned long Fact(unsigned int n)
{
	unsigned int i;
    unsigned long result=1;
	for(i=2;i<=n;i++)
		result *=i;
	return result;
}