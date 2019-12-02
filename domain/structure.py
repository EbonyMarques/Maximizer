def decision_maker():
    confirm = input(">>> ")
    print()
    if confirm.lower() == "s" or confirm.lower() == "sim":
        return 2
    elif confirm.lower() == "n" or confirm.lower() == "não":
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
    print("<!> Você definiu %i produto(s)"%(len(constants)), end="")
    for i in range(1, len(constants)+1):
        if i == len(constants) and len(constants) == 1:
            print(", x%i! "%(i))
            products.append("x%i"%(i))
        elif i == len(constants):
            print(" e x%i! "%(i))
            products.append("x%i"%(i))
        else:
            print(", x%i"%(i), end="")
            products.append("x%i"%(i))

    for i in range(1, len(constants)+1):
        if i == len(constants):
            objective += str(constants[i-1]) + "x%i" %(i)
        else:
            objective += str(constants[i-1]) + "x%i + " %(i)

    print("\n<?> z = %s representa a função objetivo? S/N?" %(objective))

    while True:
        result = decision_maker()
        if result == 0:
            print("<!> Você deve entrar com S (Sim) ou N (Não)!")
            continue
        elif result == 1:
            return 0
        elif result == 2:
            return (constants, products, objective)

def confirm_constraint(constants, name, mark):
    constraint = ""
    print("<?> Restrição de %s gerada para %i produto(s)"%(name, len(constants)-1), end="")
    for i in range(1, len(constants)):
        if i == len(constants)-1:
            print(" e x%i. "%(i))
        else:
            print(", x%i"%(i), end="")

    for i in range(1, len(constants)):
        if i == len(constants)-1:
            constraint += str(constants[i-1]) + "x%i %s " %(i, mark) + str(constants[i])
        else:
            constraint += str(constants[i-1]) + "x%i + " %(i)

    print("\n<?> %s representa a restrição de %s? S/N?" %(constraint, name))

    while True:
        result = decision_maker()
        if result == 0:
            print("<!> Você deve entrar com S (Sim) ou N (Não)!")
            continue
        elif result == 1:
            return 0
        elif result == 2:
            return constraint

def confirm_value_constraint(constant, value, mark):
    constraint = "%s %s " %(constant, mark) + str(value)
    if mark == "<=":
        print("\n<?> Restrição de Quantidade máxima gerada para 1 produto, %s."%(constant))
        print("<?> %s representa a restrição de Quantidade máxima? S/N?" %(constraint))
    else:
        print("\n<?> Restrição de Quantidade mínima gerada para 1 produto, %s."%(constant))
        print("<?> %s representa a restrição de Quantidade mínima? S/N?" %(constraint))
    while True:
        result = decision_maker()
        if result == 0:
            print("<!> Você deve entrar com S (Sim) ou N (Não)!")
            continue
        elif result == 1:
            return 0
        elif result == 2:
            return constraint

def confirm_skip():
    print("<?> Tem certeza disso? S/N?")
    while True:
        result = decision_maker()
        if result == 0:
            print("<!> Você deve entrar com S (Sim) ou N (Não)!")
            continue
        elif result == 1:
            return True
        elif result == 2:
            return False
        break