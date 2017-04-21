import math

def split(array, divisor):
    """Splits array by divisor into equally sized arrays and returns as list of
     arrays
     
     Method works by checking the input, calculating some required values then 
     entering a recursive loop to calculate and output all sub-arrays.
     """

    if len(array) < divisor:
        raise ValueError("Parameter array cannot be smaller than the divisor provided.")
    if divisor < 1:
        raise ValueError("Parameter divisor must be an integer greater than one.")
    if len(array) < 1:
        raise ValueError("Parameter array cannot be empty.")

    array_length = int(math.ceil(float(len(array)) / float(divisor)))
    return _recurse_split(array, array_length, [])

def _recurse_split(array, array_length, output):
    """Appends the next sub-array to the output and then calls itself, passing
    a modified array with the newly created sub-array removed from it. 
    
    When the array passed to it is empty, it is time to return the output which
    contains all the sub-arrays.
    """
    if len(array) == 0:
        return output

    output.append(array[0:array_length])
    return _recurse_split(array[array_length:], array_length, output)