while True:
    operator = input("Operators: \n "
                     "1 '+'\n "
                     "2 '-'\n "
                     "3 '*'\n "
                     "4 '/'\n "
                     "5 'Exponentiation'\n "
                     "6 'Division without remainder'\n "
                     "7 'Square root'\n "
                     "8 'Remainder of the division'\n "
                     "exit 'Exit from program'\n "
                     "Please choose an operator: ")
    if operator not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Can not find operator")
        continue
    if operator == "exit":
        break
    try:
        number_1 = int(input("Please type a number: "))
        if operator != "7":
            number_2 = int(input("Please type another number: "))
        if operator == "1":
            result = number_1 + number_2
        elif operator == "2":
            result = number_1 - number_2
        elif operator == "3":
            result = number_1 * number_2
        elif operator == "4":
            result = number_1 / number_2
        elif operator == "5":
            result = number_1 ** number_2
        elif operator == "6":
            result = number_1 // number_2
        elif operator == "7":
            result = number_1 // number_2
        elif operator == "8":
            result = number_1 % number_2
        else:
            print("Can not find operator")
            continue
    except ValueError:
        print("It should be a number")
        continue
    except ZeroDivisionError:
        print("You can't divide to 0")
        continue
    except Exception:
        print("Opps! Something went wrong :(")
        continue

    print("Your answer: ", result)
    answer = input("Do you want to continue? (y/n)")
    if answer.lower() == "y":
        continue
    else:
        break
