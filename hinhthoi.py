def print_diamond(height):
    if height % 2 == 0:
        height += 1 # Make sure the height is an odd number 

    n = (height + 1) // 2

    # Print the upper part of the rhombus
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    # Print the lower part of the rhombus
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

print_diamond(10)