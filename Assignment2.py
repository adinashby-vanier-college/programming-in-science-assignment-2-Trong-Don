# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    max_value = max(numbers)
    new_array = []

    for i in numbers:
        if i < max_value:
            new_array.append(i)
    
    if new_array == []:
        return (max_value, None)
    else:
        max2_value = max(new_array)

    return (max_value, max2_value)

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):

    for i in numbers:
        count = 1

        while count < 3:
            if i - numbers[count] == 0:
                numbers.remove(i)
            count += 1

        numbers.sort()

    return numbers

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    count = 1
    listing = []

    for i in arr:
        original_list = arr[:count]
        i = sum(original_list)
        listing.append(i)
        count += 1

    return listing

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    transpose = [list(row) for row in zip(*matrix)]
    
    return transpose

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    slicing = lst[0:-1:step]

    return slicing

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    result = 0

    for a, b in zip(list1, list2):
        result += a * b

    return result

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    individual_list = []
    listing1 = []
    listing2 = []

    for count in range(0, 2):
        for i in range(0, 2):
            value = 0
            for j in range(0, 2):
                value += matrix1[count][j] * matrix2[j][i]
                
            individual_list.append(value)
    
    listing1.append(individual_list[0:2])
    listing2.append(individual_list[2:4])

    return listing1 + listing2