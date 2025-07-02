from art import logo

# Making all operating/calculation typa functions
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
# Function that calculates
def calculation(first_num, second_num, operation):
    keys = {"+": add,
            "-": subtract,
            "*": multiply,
            "/": divide}
    answer = keys[operation](first_num, second_num)
    return answer

# Starts a new calculation
new_calculation = True
while new_calculation:
    print("\n" *100)
    print(logo)
    first_num = float(input("What's the first number?: "))
    continue_calculation = True
    while continue_calculation:
        print(f"+\n-\n*\n/")
        operation = input("Type a mathematical operator: ")
        second_num = float(input("What's the next number?: "))
        answer = calculation(first_num=first_num, second_num=second_num, operation=operation)
        print(f"{first_num} {operation} {second_num} = {answer}")
        # Makes first_num = answer, so that the answer value is the same if the user wants to continue the calculation
        first_num = answer
        # Asks the user whether he wants to continue or not
        choice = input(f'Type "y" to continue calculating with {answer}, or type "n" to start a new calculation: ').lower()
        if choice == "y":
            continue_calculation = True
        elif choice == "n":
            break
    # As the user chosed
    new_calculation = True












