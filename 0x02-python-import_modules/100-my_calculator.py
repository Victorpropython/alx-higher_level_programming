#!/usr/bin/python3

if __name__ == "__main__":
    """to import all function from calculator_1"""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    oprs = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(oprs.keys()):
        print("Unknown operator. Availiable operators: +, -, * and /")
        sys.exit(1)

        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print(f"{a} {sys.argv[2]} {b} = {sys.argv[2](a, b)}")
