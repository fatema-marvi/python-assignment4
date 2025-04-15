def min():
    side1 : float = float(input("Enter the length of side 1: "))
    side2 : float = float(input("Enter the length of side 2: "))
    side3 : float = float(input("Enter the length of side 3: "))

    #print the perimeter of the triangle
    perimeter : float = side1 + side2 + side3
    print("The perimeter of the triangle is " + str(perimeter) + ".")

if __name__ == "__main__":
        min()