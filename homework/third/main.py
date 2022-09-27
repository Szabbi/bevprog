def main():
    inputA = int(input("Enter 'a' value: "))
    inputB = int(input("Enter 'b' value: "))
    calc(inputA, inputB)


def calc(num1, num2):
    try:
        result = num1 / num2
        print(result)

    except ZeroDivisionError:
        print("Division by zero not allowed")
    finally:
        print("Out of try except blocks")


if __name__ == '__main__':
    main()
