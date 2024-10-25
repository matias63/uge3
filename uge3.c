#include <stdio.h>

int main()
{
    // part 1 
    // Declaring integer
    int x = 5;
    char y[] = "Hello";
    float z = 2.0;
    double k = 3.3;
 
    // Printing values
    printf("Printing Integer value %d\n", x);
    printf("Printing String value %s\n", y);
    printf("Printing Float value %.2f\n",z);
    printf("Printing double value %.4lf\n",k);


    // part 2
    int a;
    printf("Write a number ");
    scanf("%d",&a);
    
    if (a < 10){
        printf("%d is less than 10",a);
    }
    else if(a == 10){
        printf("%d equals 10",a);
    }
    else {
        printf("%d is greater than 10",a);
    }

    // part 3


    return 0;
}