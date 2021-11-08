from fractions import Fraction

#User input
rows = int(input('Number of rows\n'))
columns = int(input('Number of columns\n'))
initial = []
for i in range(rows):
    row = []
    for j in range(columns):
        coeff = eval(input('Coefficient ' + str(j + 1) + ' for row ' + str(i + 1) +  ': '))
        row.append(coeff)
    initial.append(row)
print('\nOriginal Matrix: ' + str(initial) + '\n')

#Row Echelon Conversion
def row_echelon(matrix):
    for row in range(len(matrix)):
        reorder(row, matrix)
        #find first non-zero element in each reordered row
        non_zero = 0
        while matrix[row][non_zero] == 0 and non_zero < len(matrix[row]) - 1:
            non_zero += 1

        #scale row
        scaling(row, non_zero, matrix)
        #shear rows below row
        shearing(row, non_zero, matrix)
    
    #copy matrix with floats (input for convert_to_rre)
    output = []
    for row in matrix:
        output.append(row[:])

    #convert matrix elements to fractions for printing
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            matrix[row][column] = str(Fraction(matrix[row][column]).limit_denominator())
    print('\nRow Echelon: ' + str(matrix) + '\n')
    return output

#helper functions for row_echelon
def reorder(row_i, matrix):  
    zero = False
    for column in range(len(matrix[row_i])):
        for row in range(row_i, len(matrix)):
            if matrix[row][column] != 0 and zero == False:
                hold = matrix[row_i]
                matrix[row_i] = matrix[row]
                matrix[row] = hold
                zero = True
                #print row operation
                if row != row_i:
                    op = 'R' + str(row_i + 1) + ' <=> ' + 'R' + str(row + 1) + ' : '
                    print(op + str(matrix))

def scaling(row, non_zero, matrix):
    scalar = matrix[row][non_zero]
    if scalar != 0:
        for num in range(len(matrix[row])):
            matrix[row][num] = (matrix[row][num])/scalar

        #print row operation
        frac = str(Fraction(scalar ** (-1)).limit_denominator())
        op = 'R' + str(row + 1) + ' => ' + frac + 'R' + str(row + 1) + ' : '
        print(op + str(matrix))

def shearing(row, non_zero, matrix):
    for lower in range(row + 1, len(matrix)):
        scalar_2 = matrix[lower][non_zero]
        if scalar_2 != 0:
            for element in range(len(matrix[lower])):
                shear = matrix[row][element] * scalar_2
                sheared = matrix[lower][element]
                matrix[lower][element] = shear - sheared

            #print row operation
            r_ind = 'R' + str(lower + 1)
            r_shear = 'R' + str(row + 1)
            frac = str(Fraction(scalar_2).limit_denominator())
            op = r_ind + ' => ' + frac + r_shear + ' - ' + r_ind + ' : '
            print(op + str(matrix))

#Reduced Row Echelon Conversion
def convert_to_rre(matrix):
    for row in range(len(matrix) - 1, -1 , -1):
        ech_index = 0
        while int(matrix[row][ech_index]) != 1 and ech_index < len(matrix[row]) - 1:
            ech_index += 1

        #shear rows above row
        if matrix[row][ech_index] != 0:
            backpass(row, ech_index, matrix)

    #convert matrix elements to fractions for printing
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            matrix[row][column] = str(Fraction(matrix[row][column]).limit_denominator())
    
    print('\nReduced Row Echelon: ' + str(matrix) + '\n')

#helper function for convert_to_rre
def backpass(row, ech_index, matrix):
    for upper in range(row - 1, -1, -1):
        if matrix[upper][ech_index] != 0:
            scalar_3 = matrix[upper][ech_index]
            for element in range(len(matrix[upper])):
                shear = matrix[row][element] * scalar_3
                sheared = matrix[upper][element]
                matrix[upper][element] = sheared - shear

            #print row operation
            r_ind = 'R' + str(upper + 1)
            r_shear = 'R' + str(row + 1)
            frac = str(Fraction(scalar_3).limit_denominator())
            op = r_ind + ' => ' + r_ind + ' - ' + frac + r_shear + ' : '
            print(op + str(matrix))


init = row_echelon(initial)
rre = input(('Convert to Reduced Row Echelon? (Press 1) '))
if rre == '1':
    print('')
    convert_to_rre(init)