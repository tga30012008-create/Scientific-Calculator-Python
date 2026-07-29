import math

def scientific_calculator():
    print("=== MOHAN'S ADVANCED MULTI-FUNCTION CALCULATOR ===")
    print("1. Basic Operations (+, -, *, /)")
    print("2. Trigonometry (sin, cos, tan)")
    print("3. Square Root & Power")
    print("4. Volume Calculations (Cube, Sphere, Cylinder)")
    
    choice = input("\nSelect operation category (1-4): ")

    # 1. Basic Arithmetic
    if choice == '1':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        op = input("Choose (+, -, *, /): ")
        if op == '+': print("Result:", x + y)
        elif op == '-': print("Result:", x - y)
        elif op == '*': print("Result:", x * y)
        elif op == '/': print("Result:", x / y if y != 0 else "Cannot divide by zero")

    # 2. Trigonometry
    elif choice == '2':
        angle = float(input("Enter angle in degrees: "))
        rad = math.radians(angle) # Converts degree to radian
        func = input("Choose (sin, cos, tan): ").lower()
        if func == 'sin': print(f"sin({angle}°):", math.sin(rad))
        elif func == 'cos': print(f"cos({angle}°):", math.cos(rad))
        elif func == 'tan': print(f"tan({angle}°):", math.tan(rad))

    # 3. Square Root & Power
    elif choice == '3':
        num = float(input("Enter number: "))
        opt = input("Choose (sqrt, power): ").lower()
        if opt == 'sqrt': print("Square Root:", math.sqrt(num))
        elif opt == 'power':
            p = float(input("Enter power/exponent: "))
            print("Result:", math.pow(num, p))

    # 4. Volume Calculations
    elif choice == '4':
        print("Shapes: 1. Cube | 2. Sphere | 3. Cylinder")
        shape = input("Select shape (1-3): ")
        if shape == '1':
            side = float(input("Enter side length: "))
            print("Volume of Cube:", side ** 3)
        elif shape == '2':
            r = float(input("Enter radius: "))
            print("Volume of Sphere:", (4/3) * math.pi * (r ** 3))
        elif shape == '3':
            r = float(input("Enter radius: "))
            h = float(input("Enter height: "))
            print("Volume of Cylinder:", math.pi * (r ** 2) * h)

# Function Run
scientific_calculator()
