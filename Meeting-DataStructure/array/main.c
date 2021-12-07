#include "stdio.h"

#include "array.h"

// Make sure to write DECLARE_ARRAY before DEFINE_ARRAY! 
DECLARE_ARRAY(int)
DEFINE_ARRAY(int)


void print_array(int, ARRAY(int)* array) // define our own print
{
    printf("[ ");
    for (int i = 0; i < array->count; i++)
    {
        printf("%d ", array->items[i]);
    }
    printf("]");
}

int main(int argc, char *argv[])
{
    ARRAY(int) my_array;

    init_array(int, &my_array);

    for (int i = 0; i < 10; i++)
    {
        write_array(int, &my_array, i);
    }

    print_array(int, &my_array);

    free_array(int, &my_array);
    
    return 0;
}
