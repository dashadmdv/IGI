def calculation(a, b, operation):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Wrong input! Try input numbers!")
        return None

    match operation:
        case "add":
            return a + b
        case "sub":
            return a - b
        case "mult":
            return a * b
        case "div":
            try:
                return a / b
            except ZeroDivisionError:
                print("Error! Can not divide by zero!")
                return None
        case _:
            print("Wrong operation!")
            return None
