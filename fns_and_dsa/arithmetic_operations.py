def perform_operation(num1, num2, operation):
    """
    Performs an arithmetic operation on two numbers.

    Parameters:
        num1 (float): First number
        num2 (float): Second number
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'

    Returns:
        float or str: Result of the arithmetic operation,
                      or an error message for invalid operation or division by zero.
    """

    if operation == 'add':
        result = num1 + num2
        return result

    elif operation == 'subtract':
        result = num1 - num2
        return result
    
    elif operation == 'multiply':
        result = num1 * num2
        return result

    elif operation == 'divide':
        if num2 == 0:
            return "Error, cannot divide by zero"
        result = num1 / num2
        return result
    else:
        return "Error: Invalid operation. Please choose add, subtract, multiply, or divide."
