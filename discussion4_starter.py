class Rectangle():
    # Create the constructor "__init__" method
    # Arguments: width (an ingeter), height (an integer)
    # 
    # It sets an instance variable, "width" to the passed argument, width
    # It sets an instance variable, "height" to the passed argument, height

    def __init__(self, initW, initH):
        self.w = initW #this is the width variable
        self.h = initH #this is the height variable 



    # Create the "__str__" method
    #
    # It returns a string, 
    #       "A rectangle with width ____ and height ____"

    def __str__(self):
        return "A rectangle with width" + str(self.w) + "and height" + str(self.h)



    # Create the "verify_input" method
    #
    # It returns a boolean
    #       True if the width and height are positive numbers
    #       False otherwise

    def verify_input(self):




    # Create the "area" method
    #
    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the area of the rectangle.

    def area(self):



    # Create the "perimeter" method
    #
    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the perimeter of the rectangle.

    def perimeter(self):
    


def main():
    r = Rectangle(10, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

    r = Rectangle(0, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

if __name__ == "__main__":
    main()