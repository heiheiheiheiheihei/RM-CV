#include<stdio.h>
#include<time.h>
#include<stdlib.h>
main()
{
    int a[10],i=0,j,temp;
    srand(time(NULL));
    while(i<10){
        a[i]=1+rand()%100;
        i++;
    }
    printf("原数:\n");
    for(i=0;i<10;i++)
        printf("%d\t",a[i]);
    for(i=0;i<9;i++)            //排序（倒序）
        for(j=0;j<9-i;j++){
            if(a[j]<a[j+1]){
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    printf("倒序：\n");
    for(i=0;i<10;i++)
        printf("%d\t",a[i]);
    return 0;
}




