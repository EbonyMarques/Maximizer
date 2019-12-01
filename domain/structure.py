def input_handler(text):
    if len(text) == 0:
        return 0
    try:
        result = text.split(",")
        for i in range(0, len(result)):
            result[i] = float(result[i].strip())
    except:
        result = 0
    return result

def decision_maker():
    confirm = input(">>> ")
    if confirm.lower() == "s":
        return 2
    elif confirm.lower() == "n":
        return 1
    else:
        return 0

def input_objective(message):
    raw = input(message)
    return input_handler(raw)

def confirm_objective(constants):
    objective = ""
    products = []
    print("\n<?> Considerando que você setou %i produtos"%(len(constants)), end="")
    for i in range(1, len(constants)+1):
        if i == len(constants):
            print(" e x%i, "%(i))
            products.append("x%i"%(i))
        else:
            print(", x%i"%(i), end="")
            products.append("x%i"%(i))

    for i in range(1, len(constants)+1):
        if i == len(constants):
            objective += str(constants[i-1]) + "x%i" %(i)
        else:
            objective += str(constants[i-1]) + "x%i + " %(i)

    print("<?> z = %s representa a função objetivo? s/n?" %(objective))

    while True:
        result = decision_maker()
        if result == 0:
            print("<!> Você deve entrar com s (sim) ou n (não)!")
            continue
        elif result == 1:
            return 0
        elif result == 2:
            return (constants, products)

def set_objective():
    objective = ""
    products = []
"""
def set_constraint(constraint_obj, a):
    print("\n<!> Vamos à restrição de %s."%constraint_obj.name)

    raw_constants = input(constraint_obj.message1)
    constants = raw_constants.strip().split(",")
    constraint = ""

    for i in range(0, len(constants)):
        constants[i] = float(constants[i].strip())

    if len(constants) != len(a):
        return 0

    for i in range(0, len(constants)):
        constraint += str(constants[i]) + ","

    constraint = constraint[:-1]

    while True:
        b = input(constraint_obj.message2)
        if b.lower() == "menor":
            constraint += "L"
        elif b.lower() == "maior":
            constraint += "G"
        else:
            print(constraint_obj.error2)
            continue
        break

    while True:
        try:
            b = float(input(constraint_obj.message3))
            constraint += str(b)
        except:
            print(constraint_obj.error3)
            continue
        break

    return constraint
"""
def set_constraint(name, message, a):
    print("\n<!> Vamos à restrição de %s."%name)

    raw_constants = input(message)
    constants = raw_constants.strip().split(",")

    #print(constants)

    for i in range(0, len(constants)):
        constants[i] = float(constants[i].strip())

    if len(constants) != len(a)+1:
        return 0

    return constants

def set_constraint_2(message, a, product):
    try:
        constant = float(input(message + product +": "))
        return constant
    except Exception as e:
        print(e)