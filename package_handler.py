import sys
from tests import run_tests

def sort_package(width, height, length, mass):
    # Calculate volume and check individual dimension constraints
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
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

if __name__ == "__main__":
    main()
