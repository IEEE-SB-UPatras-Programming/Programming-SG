#ifndef array_h
#define array_h

#include "stdlib.h"

#define ARRAY(type) struct _array_##type

#define DEFINE_ARRAY(type)                                                                \
    void _init_array_##type(ARRAY(type) * array)                                          \
    {                                                                                     \
        array->capacity = 0;                                                              \
        array->count = 0;                                                                 \
        array->items = NULL;                                                              \
    }                                                                                     \
    void _write_array_##type(ARRAY(type) * array, type val)                               \
    {                                                                                     \
        if (array->capacity < array->count + 1)                                           \
        {                                                                                 \
            array->capacity = !array->capacity ? 1 : array->capacity * 2;                 \
            array->items = (type *)realloc(array->items, array->capacity * sizeof(type)); \
        }                                                                                 \
        array->items[array->count] = val;                                                 \
        array->count++;                                                                   \
    }                                                                                     \
    void _free_array_##type(ARRAY(type) * array)                                          \
    {                                                                                     \
      free(array->items);                                                                 \
      init_array(type, array);                                                            \
    }                                                                                     \

#define DECLARE_ARRAY(type)                                                               \
    struct _array_##type                                                                  \
    {                                                                                     \
        int capacity;                                                                     \
        int count;                                                                        \
        type* items;                                                                      \
                                                                                          \
    };                                                                                    \
    void _init_array_##type (ARRAY(type)* array);                                         \
    void _write_array_##type(ARRAY(type)* array, type val);                               \
    void _free_array_##type (ARRAY(type)* array);                                         \

#define init_array(type, array) _init_array_##type(array)
#define write_array(type, array, val) _write_array_##type(array, val)
#define free_array(type, array) _free_array_##type(array)
#define print_array(type, array) _print_array_##type(array)

#endif // array_h
