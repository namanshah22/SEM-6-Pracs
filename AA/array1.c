#include <stdio.h>

#define MAX_SIZE 10

// Array structure
typedef struct {
    int arr[MAX_SIZE];
    int size;
} Array;

// Function prototypes
void append(Array *arr, int value);
void remove_element(Array *arr, int value);
int find_indx(Array *arr, int value);

int main() {
    Array arr = {{1, 2, 3}, 3};
    int i, index;

    // Print array elements
    printf("Array elements: ");
    for (i = 0; i < arr.size; i++) {
        printf("%d ", arr.arr[i]);
    }
    printf("\n");

    // Append element to array
    append(&arr, 4);
    printf("Array after appending element 4: ");
    for (i = 0; i < arr.size; i++) {
        printf("%d ", arr.arr[i]);
    }
    printf("\n");

    // Remove element from array
    remove_element(&arr, 2);
    printf("Array after removing element 2: ");
    for (i = 0; i < arr.size; i++) {
        printf("%d ", arr.arr[i]);
    }
    printf("\n");

    index = find_indx(&arr, 3);
    printf("%d\n", index);

    return 0;
}

// Append element to array
void append(Array *arr, int value) {
    if (arr->size < MAX_SIZE) {
        arr->arr[arr->size] = value;
        arr->size++;
    } else {
        printf("Array is full. Cannot append.\n");
    }
}

// Remove element from array
void remove_element(Array *arr, int value) {
    int i, j;
    for (i = 0; i < arr->size; i++) {
        if (arr->arr[i] == value) {
            for (j = i; j < arr->size - 1; j++) {
                arr->arr[j] = arr->arr[j + 1];
            }
            arr->size--;
            return;
        }
    }
    printf("Element not found. Cannot remove.\n");
}

int find_indx(Array *arr, int value) {
    int i;
    for (i = 0; i < arr->size; i++) {
        if (arr->arr[i] == value) {
            return i;
        }
    }
    return -1; // Element not found
}
