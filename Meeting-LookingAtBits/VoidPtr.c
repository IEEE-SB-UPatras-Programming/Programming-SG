#include <stdio.h>

enum Type 
{
   INT,
   CHAR,
   STRING,
};

struct MyStruct 
{
    void * data;
    int type;
};



void DoSomethingInt(int n)
{

}

void DoSomethingChar(char c)
{

}

void DoSomething(struct MyStruct * something)
{
    
    switch(something->type)
    {
        case (INT):
            printf("%d", *(int *)something -> data); break;

        case (CHAR):
            printf("%c", *(char *)something -> data); break;

        case (STRING):
            printf("%s", (char *)something -> data); break;

        default:
            break;
    }

}

int main()
{
    int n = 97;

    struct MyStruct s1, s2;

    s1.data = &n;
    s1.type = INT;

    s2.data = &n;
    s2.type = CHAR;

    char a[] = "Ioanna";

    struct MyStruct myList[] = { 
        { &n, INT }, 
        { &n, CHAR }, 
        { a,  STRING},
        {NULL, NULL},
    };


    for (int i = 0; myList[i].data || myList[i].type; i++)
    {
        DoSomething(&myList[i]);
        printf("\n");
    }


    return 0;
}
