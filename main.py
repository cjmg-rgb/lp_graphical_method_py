from fractions import Fraction
import math


def lcm(a, b):
    # Get the least common multiplier
    return abs(a * b) // math.gcd(a, b)


def graphical_method(z, c1, c2):
    # Removes unwanted characters
    translation = str.maketrans({"+": " ", "x": "", "y": "", " ": "", "=": " ", "<": "", ">": ""})
    z = z.translate(translation).split(" ")
    c1 = c1.translate(translation).split(" ")
    c2 = c2.translate(translation).split(" ")

    # Creates a list each constraints with just a number
    z_x, z_y = [float(x) for x in z]
    const_1 = [float(x) for x in c1]
    const_2 = [float(x) for x in c2]

    constants = [const_1, const_2]

    # Creates coordinates of each constants that will be used to find the feasible region
    coordinates = []

    for constant in constants:
        x = constant[2] / constant[0]
        y = constant[2] / constant[1]
        coordinates.append([(x, 0), (0, y)])

    # Get the minimum X and Y
    least_x = coordinates[0][0][0] if coordinates[0][0][0] < coordinates[1][0][0] else coordinates[1][0][0]
    least_y = coordinates[0][1][1] if coordinates[0][1][1] < coordinates[1][1][1] else coordinates[1][1][1]

    # Get the LCM for multipliers
    generated_lcm = lcm(int(c1[0]), int(c2[0]))

    c1_multiplier = generated_lcm / float(c1[0])
    c2_multiplier = generated_lcm / float(c2[0])

    c1 = [float(x) * c1_multiplier for x in c1]
    c2 = [float(x) * c2_multiplier for x in c2]

    # Calculation for getting the 3rd point's x and y
    p3_y = 0

    for i in range(len(c1) - 1):
        p3_y += (c1[i] - c2[i])

    p3_y = (c1[2] - c2[2]) / p3_y

    p3_x = abs((constants[0][2] - (c1[1] * p3_y)) / c1[0])

    # Final Points
    points = [
        (0, 0),
        (0, least_y),
        (p3_x, p3_y),
        (least_x, 0),
    ]


    # Final calculation to get the largest, the x and the y
    largest = 0
    index = 0
    found_at = 0

    for p in points:
        x, y = p
        temp = (x * z_x) + (y * z_y)
        if temp > largest:
            largest = temp
            found_at = index
        index += 1

    conclusion = (points[found_at][0], points[found_at][1], largest)

    return conclusion


def main():
    # Without Fraction (98% accuracy/Working)
    z = "20x + 18y"
    c1 = "5x + 4y <= 27000"
    c2 = "5x + 15y <= 43200"

    # With Fraction (to be fixed)
    # z = "50x + 60y"
    # c1 = "2x + 5y <= 50"
    # c2 = "8x + 6y <= 120"

    max_x, max_y, max_total = graphical_method(z, c1, c2)
    print(z)
    print(f"X: {max_x}\nY: {max_y}\nTotal: {max_total}")


if __name__ == "__main__":
    main()
