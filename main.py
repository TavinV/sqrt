square = float(input("Chose a number for calculating the square root: "))

# initial guess
square_root = 1

n_iterations = int(input("How many iterations? "))

for i in range(n_iterations):
    print(square_root)
    square_root = 0.5*(square_root + (square/square_root))

print(f'sqrt of {square} is {square_root}')