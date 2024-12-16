from package_handler import sort_package

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