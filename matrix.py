import random


# Create and return matrix raw
def create_matrix_raw():
    raw = []
    [raw.append(random.randint(-9, 9)) for num in range(10)]
    return raw


# Create and return 2-dimensions matrix
def create_matrix():
    matrix = [create_matrix_raw() for raw in range(10)]
    return matrix, "Matrix length is: %d" % len(matrix)


# Here we get a tuple with 2 elements(matrix & matrix length)
matrix = create_matrix()


# Display matrix in console
def display_matrix(matrix):
    for raw in matrix[0]:
        print raw
    print "*" * 80
    print matrix[1]
    print "*" * 80

print "Displaying our matrix"
print "*" * 80
display_matrix(matrix)


# Find random matrix raw
random_raw_num = random.randint(0, len(matrix))


def find_raw(matrix, random_raw_num):
    return matrix[0][random_raw_num]

raw = find_raw(matrix, random_raw_num)


# Find random matrix column
random_col_num = random.randint(0, len(matrix))


def find_col(matrix, random_col_num):
    column = []
    for item in matrix[0]:
        column.append(item[random_col_num])
    return column

column = find_col(matrix, random_col_num)


# Function that takes two lists and multiply them
def lists_multiply(list_1, list_2):
    if len(list_1) == len(list_2):
        common_list = []
        for item in range(len(list_1)):
            common_list.append(list_1[item] * list_2[item])
        mult_result = 1
        for num in common_list:
            mult_result *= num
    return mult_result

mult_result = lists_multiply(raw, column)


# Function that calculate intersection of raw and column
def intersect(matrix):
    results = []
    counter = 0
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix[0])):
            i_raw = find_raw(matrix, i)
            j_column = find_col(matrix, j)
            divider = i_raw[j]
            results.append(lists_multiply(i_raw, j_column))
            try:
                results[counter] = results[counter] / divider
            except ArithmeticError:
                results[counter] = 0
            counter += 1
    return results


intersections = intersect(matrix)


# Find the three minimum values
def find_minimum(intersections):
    return [min(intersections) for i in range(3)]

print "Three minim values of perpendicular intersection in the matrix are: "
print find_minimum(intersections)
