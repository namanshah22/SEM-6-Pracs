def main():
    arr = []

    # Append elements to array
    arr.append(1)
    arr.append(2)
    arr.append(3)

    # Print array elements
    print("Array elements:", end=" ")
    for elem in arr:
        print(elem, end=" ")
    print()

    # Remove an element from array
    arr.remove(2)
    print("Array after removing element 2:", arr)

    indx = arr.index(3)
    print("Index of element 3:", indx)

if __name__ == "__main__":
    main()
