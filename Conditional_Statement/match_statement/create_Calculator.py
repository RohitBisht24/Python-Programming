num1, ope, num2 = input(
    "Enter the Calcualation(+, -, *, /, %, ** ) : ").split()
a = int(num1)
b = int(num2)

match ope:
    case "+": print("sum is : ", a + b)
    case "-": print("minus is : ", a - b)
    case "*": print("multiply is : ", a * b)
    case "/": print("divide is : ", a / b)
    case "//": print("divide is : ", a // b)
    case "%": print("remainder is : ", a % b)
    case "**": print("power is : ", a ** b)
    case _: print("Invalid Calculation!")
