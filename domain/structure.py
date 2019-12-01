def decision_maker():
    confirm = input(">>> ")
    if confirm.lower() == "s":
        return 2
    elif confirm.lower() == "n":
        return 1
    else:
        return 0

def input_costs(message):
    raw = input(message)
    try:
        result = raw.split(",")
        for i in range(0, len(result)):
            result[i] = float(result[i].strip())
        return result
    except:
        return 0

def input_constraints(message, product):
    try:
        return float(input(message + product +": "))
    except:
        return False

def confirm_objective(constants):
    objective = ""
    products = []
    print("\n<?> Considerando que você definiu %i produto(s)"%(len(constants)), end="")
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
            return (constants, products, objective)

def confirm_constraint(constants, name, mark):
    constraint = ""
    print("\n<?> Essas são as restrições para o(s) %i produto(s)"%(len(constants)), end="")
    for i in range(1, len(constants)+1):
        if i == len(constants):
            print(" e x%i, "%(i))
        else:
            print(", x%i"%(i), end="")

    for i in range(1, len(constants)):
        if i == len(constants)-1:
            constraint += str(constants[i-1]) + "x%i %s " %(i, mark) + str(constants[i])
        else:
            constraint += str(constants[i-1]) + "x%i + " %(i)

    print("<?> %s representa a restrição de %s? s/n?" %(constraint, name))

    while True:
        result = decision_maker()
        if result == 0:
            print("<!> Você deve entrar com s (sim) ou n (não)!")
            continue
        elif result == 1:
            return 0
        elif result == 2:
            return constraint

def confirm_value_constraint(constant, value, mark):
    print("\n<?> Essa é a restrição para o produto %s"%(constant))

    constraint = "%s %s " %(constant, mark) + str(value)

    print("<?> %s , confirma? s/n?" %(constraint))

    while True:
        result = decision_maker()
        if result == 0:
            print("<!> Você deve entrar com s (sim) ou n (não)!")
            continue
        elif result == 1:
            return 0
        elif result == 2:
            return constraint

def confirm_skip():
    print("<?> Tem certeza disso? s/n?")
    while True:
        result = decision_maker()
        if result == 0:
            print("<!> Você deve entrar com s (sim) ou n (não)!")
            continue
        elif result == 1:
            return True
        elif result == 2:
            return False
        break