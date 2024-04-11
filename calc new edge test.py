def greeting():
    while True:
        name = input("What is your name? ").title().strip()
        if " " in name:
            first_name, last_name = name.split()
            break
        else:
            print("Please enter your full name.")
    print(f"Hey, {first_name} let's do some math!")
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a valid number. Please try again.")
def get_expression():
    while True:
        expression = input("Enter an arithmetic expression (+,-,*,/): ").strip()
        if expression in ["+", "-", "*", "/"]:
            return expression
        else:
            print("That's not a valid expression. Please enter an arithmetic expression (+,-,*,/).")

def main():
    x=get_int_input("Enter a number: ")
    expression = get_expression()
    y=get_int_input("Enter a another number: ")
    if expression=="+": print("Easy! Your answer is, ", (x+y))
    elif expression=="-": print("right! Your answer is ", (x-y))
    elif expression=="*": print("I think I got this! It's ", (x*y))
    elif expression=="/":
        try: print("Tricky! Is it ", (x/y),"?")
        except ZeroDivisionError: print("Sorry! You can't divide by zero!")
def hello(to = "stranger"):
    print(f"Hello {to}")
def repeat():
    while True:
        loop = input("Would you like to do another calculation? (y/n) ").lower()
        if loop == "y":
            main()
        elif loop == "n":
            print("Thank you! Come back soon!")
            break
        else: print("Please enter either 'y' or 'n'.")

hello()
greeting()
main()
repeat()

