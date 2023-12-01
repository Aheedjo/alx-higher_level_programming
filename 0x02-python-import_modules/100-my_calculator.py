#!/usr/bin/python3


if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    argc = len(argv)
    ops = ["+", "-", "*", "/"]

    if (argc != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if (argv[2] not in ops):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = str(argv[2])

    if (op == '+'):
        result = add(int(a), int(b))

    elif (op == '-'):
        result = sub(int(a), int(b))

    elif (op == '*'):
        result = mul(int(a), int(b))
    else:
        result = div(int(a), int(b))

    print(f"{a} {op} {b} = {result}")
