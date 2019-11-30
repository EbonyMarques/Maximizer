def set_objective(message):
    print(message)
    constants_raw = input(">>> Entre com os lucros de cada produto: ")
    constants = constants_raw.strip().split(",")
    objective = ""

    for i in range(0, len(constants)):
        constants[i] = int(constants[i].strip())

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

    print("<?> z = %s representa a função objetivo? " %(objective), end="")

    while True:
        confirm = input("S/N: ")
        if confirm.lower() == "s":
            return (constants, objective, products)
        elif confirm.lower() == "n":
            return 0
        else:
            print("<!> Confirme com S/N!")
            continue
"""
def set_constraint(constraint_obj, a):
    print("\n<!> Vamos à restrição de %s."%constraint_obj.name)

    constants_raw = input(constraint_obj.message1)
    constants = constants_raw.strip().split(",")
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
def set_constraint(constraint_obj, a):
    print("\n<!> Vamos à restrição de %s."%constraint_obj.name)

    constants_raw = input(constraint_obj.message1)
    constants = constants_raw.strip().split(",")
    constraint = ""

    print(constants)

    for i in range(0, len(constants)):
        constants[i] = float(constants[i].strip())

    if len(constants) != len(a):
        return 0

    for i in range(0, len(constants)):
        constraint += str(constants[i]) + ","

    #constraint = constraint[:-1]
    constraint += "L,"

    while True:
        try:
            b = float(input(constraint_obj.message3))
            constraint += str(b)
        except:
            print(constraint_obj.error3)
            continue
        break

    #constraint_obj.constraint = constraint
    return constraint

def set_constraint_2(constraint_obj, a, product, condc):
    try:
        constant = float(input(constraint_obj.message1 + product +": "))
        b = [0]*len(a)
        c = product[1:]
        b[int(c)-1] = 1

        constraint = ""
        for i in b:
            constraint += str(i) + ","
        #constraint = constraint[:-1]
        constraint += "%s," %(condc) + str(constant) 
        
        #constraint_obj.constraint = constraint
        return constraint
    except Exception as e:
        print(e)
        #print(constraint_obj.error1)

    """
    for i in range(1, len(constants)+1):
        if i == len(constants):
            constraint += str(constants[i-1]) + "x%i" %(i)
        else:
            constraint += str(constants[i-1]) + "x%i + " %(i)

    confirm = input("s/n: ")
    if confirm.lower() == "s":
        return 1
    else:
        return 0
    """