from fractions import Fraction
from typing import List


# Row Echelon Conversion
def row_echelon(matrix: List[List[float]]) -> List[List[float]]:
    for row in range(len(matrix)):
        reorder(row, matrix)
        # find first non-zero element in each reordered row
        non_zero = 0
        while matrix[row][non_zero] == 0 and non_zero < len(matrix[row]) - 1:
            non_zero += 1

        # scale row
        scaling(row, non_zero, matrix)
        # shear rows below row
        shearing(row, non_zero, matrix)

    print('\nRow Echelon: ')
    l = fractionalize(matrix)
    for row in l:
        print(str(row))
    print('')

    return matrix


# helper functions for row_echelon
def reorder(row_i: int, matrix: List[List[float]]) -> None:
    zero = False
    for column in range(len(matrix[row_i])):
        for row in range(row_i, len(matrix)):
            if matrix[row][column] != 0 and zero == False:
                hold = matrix[row_i]
                matrix[row_i] = matrix[row]
                matrix[row] = hold
                zero = True
                # print row operation
                if row != row_i:
                    op = 'R' + str(row_i + 1) + ' <=> ' + 'R' + str(row + 1) + ' : '
                    print(op + str(fractionalize(matrix)))


def scaling(row: int, non_zero: int, matrix: List[List[float]]) -> None:
    scalar = matrix[row][non_zero]
    if scalar != 0:
        for num in range(len(matrix[row])):
            matrix[row][num] = (matrix[row][num])/scalar

        # print row operation
        frac = str(Fraction(scalar ** (-1)).limit_denominator())
        op = 'R' + str(row + 1) + ' => ' + frac + 'R' + str(row + 1) + ' : '
        print(op + str(fractionalize(matrix)))


def shearing(row: int, non_zero: int, matrix: List[List[float]]) -> None:
    for lower in range(row + 1, len(matrix)):
        scalar_2 = matrix[lower][non_zero]
        if scalar_2 != 0:
            for element in range(len(matrix[lower])):
                shear = matrix[row][element] * scalar_2
                sheared = matrix[lower][element]
                matrix[lower][element] = shear - sheared

            # print row operation
            r_ind = 'R' + str(lower + 1)
            r_shear = 'R' + str(row + 1)
            frac = str(Fraction(scalar_2).limit_denominator())
            op = r_ind + ' => ' + frac + r_shear + ' - ' + r_ind + ' : '
            print(op + str(fractionalize(matrix)))


# Reduced Row Echelon Conversion
def convert_to_rre(matrix: List[List[float]]) -> None:
    for row in range(len(matrix) - 1, -1 , -1):
        ech_index = 0
        while int(matrix[row][ech_index]) != 1 and ech_index < len(matrix[row]) - 1:
            ech_index += 1

        #shear rows above row
        if matrix[row][ech_index] != 0:
            backpass(row, ech_index, matrix)

    # print('\nReduced Row Echelon: ' + str(fractionalize(matrix)) + '\n')
    print('\nReduced Row Echelon: ')
    l = fractionalize(matrix)
    for row in l:
        print(str(row))


# helper function for convert_to_rre
def backpass(row: int, ech_index: int, matrix: List[List[float]]) -> None:
    for upper in range(row - 1, -1, -1):
        if matrix[upper][ech_index] != 0:
            scalar_3 = matrix[upper][ech_index]
            for element in range(len(matrix[upper])):
                shear = matrix[row][element] * scalar_3
                sheared = matrix[upper][element]
                matrix[upper][element] = sheared - shear

            # print row operation
            r_ind = 'R' + str(upper + 1)
            r_shear = 'R' + str(row + 1)
            frac = str(Fraction(scalar_3).limit_denominator())
            op = r_ind + ' => ' + r_ind + ' - ' + frac + r_shear + ' : '
            print(op + str(fractionalize(matrix)))


def fractionalize(matrix: List[List[float]]) -> List[List[str]]:
    '''Return fractionalized matrix for print statments'''
    p_matrix = []
    for row in matrix:
        p_matrix.append(row[:])
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            p_matrix[row][column] = str(Fraction(matrix[row][column]).limit_denominator())

    return p_matrix


if __name__ == "__main__":
    # User input
    rows = int(input('Number of rows\n'))
    columns = int(input('Number of columns\n'))
    initial = []
    for i in range(rows):
        row = []
        for j in range(columns):
            coeff = eval(input('Coefficient ' + str(j + 1) + ' for row ' + str(i + 1) + ': '))
            row.append(coeff)
        initial.append(row)
    # print('\nOriginal Matrix: ' + str(initial) + '\n')
    print('\nOriginal Matrix: ')
    l = fractionalize(initial)
    for row in l:
        print(str(row))
    print('')

    init = row_echelon(initial)
    rre = input('Convert to Reduced Row Echelon? (Press 1) ')
    if rre == '1':
        print('')
        convert_to_rre(init)
