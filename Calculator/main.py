from art import logo

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculate():
    print(logo)
    num1 = int(input("Please enter your first number: "))
    should_accumulate = True


    while should_accumulate:
        for symbol in operations:
            print(symbol)
        choice=input(f"Which operation would you like to perform?")
        num2 = int(input("Please enter your second number: "))
        answer = operations[choice](num1, num2)
        print(f"{num1} {choice} {num2} = {answer}")

        continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if continue_calculation == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculate()
calculate()
