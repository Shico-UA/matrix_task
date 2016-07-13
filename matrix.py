import random

# Create and return matrix raw
def create_matrix_raw():
    raw = []
    [raw.append(random.randint(0, 9)) for num in range(10)]
    return raw


# Create and return 2-dimensions matrix
def create_matrix():
    matrix = [create_matrix_raw() for raw in range(10)]
    return matrix, "Matrix length is: %d" % len(matrix)

# Here we get a tuple with 2 elements(matrix & matrix length)
matrix = create_matrix()


# Display matrix in console
def display_matrix(matrix):
    for raw in matrix[0]: print raw
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

print "Random raw from our matrix: %s" % find_raw(matrix, random_raw_num)
print "*" * 80
    
# Find random matrix column
random_col_num = random.randint(0, len(matrix))
def find_col(matrix, random_col_num):
    column = []
    for item in matrix[0]:
        column.append(item[random_col_num])
    return column

print "Random column from our matrix: %s" % find_col(matrix, random_col_num)
print "*" * 80





