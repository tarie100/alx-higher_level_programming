#!/usr/bin/python3
def safe_print_division(a, b):
    quotient = (a / b)
    try:
        print("{}".format(quotient, end=""))
    except ArithmeticError:
        raise
    else:
        return None
    finally:
        print()
        return quotient
