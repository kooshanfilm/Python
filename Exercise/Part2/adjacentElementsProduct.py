'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.

Input/Output

[time limit] 4000ms (py3)

[input] array.integer inputArray
An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer <br > The largest product of adjacent elements.

'''

def adjacentElementsProduct(inputArray):
    len_arr = len(inputArray)
    max = -1000
    for i in range(0, len_arr - 1):
        if inputArray[i] * inputArray[i+1] > max:
            max = inputArray[i] * inputArray[i+1]

    return (max)

adjacentElementsProduct([-23, 4, -3, 8, -12])