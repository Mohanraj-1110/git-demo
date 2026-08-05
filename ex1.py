def greet(name):
    return f"Hello, {name}! Welcome to the Python program."


def add_numbers(a, b):
    return a + b


def main():
    name = input("Enter your name: ")
    print(greet(name))

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print(f"Sum: {add_numbers(x, y)}")
    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
