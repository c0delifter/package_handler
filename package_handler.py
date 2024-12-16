import sys

def sort_package(width, height, length, mass):
    # Calculate volume and check individual dimension constraints
    volume = width * height * length
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    # Determine package label based on conditions
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

def main():
    args = sys.argv
    if len(args) > 1:
        if args[1] == "--dimensions" and len(args) == 6:
            try:
                width = int(args[2])
                height = int(args[3])
                length = int(args[4])
                mass = int(args[5])
                result = sort_package(width, height, length, mass)
                print(f"The package is: {result}")
            except ValueError:
                print("Invalid dimensions or mass. Please provide valid integers.")
        elif args[1] == "--tests":
            run_tests()
        else:
            print("Invalid arguments. Use --dimensions <width> <height> <length> <mass> or --tests.")
    else:
        print("No arguments provided. Use --dimensions <width> <height> <length> <mass> or --tests.")

def run_tests():
    tests = [
        {"width": 100, "height": 100, "length": 100, "mass": 10, "expected": "STANDARD"},  # Neither bulky nor heavy
        {"width": 200, "height": 50, "length": 40, "mass": 10, "expected": "SPECIAL"},   # Bulky only
        {"width": 50, "height": 50, "length": 50, "mass": 25, "expected": "SPECIAL"},   # Heavy only
        {"width": 200, "height": 200, "length": 200, "mass": 25, "expected": "REJECTED"} # Both bulky and heavy
    ]

    for i, test in enumerate(tests):
        result = sort_package(test["width"], test["height"], test["length"], test["mass"])
        print(f"Test {i + 1}: {'PASS' if result == test['expected'] else 'FAIL'} | Expected: {test['expected']}, Got: {result}")

if __name__ == "__main__":
    main()
