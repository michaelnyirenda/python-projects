from art import logo
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2
def exp(n1, n2):
    return n1 ** n2
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
    "^": exp
}

def calculator():
    print(logo)
    num1 = float(input("what's the first number? : "))
    for operators in operations:
        print(operators)
    should_continue = True
    
    while should_continue == True:
        operator = input("pick an operation: ")
        num2 = float(input("what's the next number? : "))
        calculation = operations[operator] 
        answer = calculation(num1, num2)
        
        print(f"{num1} {operator} {num2} = {answer}")
        
        if input(f"type 'y' to continue calulating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator() 
          
calculator()            
