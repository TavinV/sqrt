def square_root(square: float, n_iterations: int) -> float:
    """Evaluates the square root of the given input, for n iterations,
    with the babylonian method\n
    Parameters:
        square (float): the square
        n_iterations (int): the number of iterations for the algorithm
    Returns:
        float: the square root of the input"""
    
    # initial guess
    square_root = 1
    
    # iterates the algorithm
    for i in range(n_iterations):
        print(square_root)
        square_root = 0.5*(square_root + (square/square_root))

    print(f'sqrt of {square} is {square_root}')

    return square_root

def main():
    square = float(input("Chose a number for calculating the square root: "))
    n_iterations = int(input("How many iterations? "))
    square_root(square=square, n_iterations=n_iterations)

main()