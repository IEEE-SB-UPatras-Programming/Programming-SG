#include "stdio.h"

typedef struct {

    int n;

} Base;

typedef struct {

    Base b;
    int o;

} BaseOnBase;

typedef struct {

    int n;
    int k;
    char c;

} Small;

typedef struct {

    Small s;
    int o;

} Bigger;

int main()
{

    BaseOnBase baseOn;    
    baseOn.b.n = 123;
    baseOn.o = 123;

    BaseOnBase* baseOnPtr = &baseOn;

    Base* basePtr = (Base*)(baseOnPtr);

    printf("Number: %d, %d\n", basePtr->n, sizeof(BaseOnBase));
    
    printf("Extra space: %d\n", sizeof(Bigger));

    printf("%d\n", 100);
    printf("%c\n", 100);

    printf("%c\n", 'a');
    printf("%d\n", 'a');

    printf("%d\n", (int)3.14);

    float f = 3.14;

    printf("%d\n", *(int*)(&f));


    float floatArray[] = { 
                        1.1431391224375825e+27,
                        3218.027099609375,
                        3.055420598881582e-39,
                        };

    printf("%s\n", floatArray); 
    return 0;
}
