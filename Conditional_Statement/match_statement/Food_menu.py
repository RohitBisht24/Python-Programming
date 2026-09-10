menu = int(input("Enter your food menu : "))

match menu:
    case 1: print("Pizza")
    case 2: print("Burger")
    case 3: print("Momos")
    case 4: print("Cold coffee")
    case _: print("ye Food Menu main nhi ")