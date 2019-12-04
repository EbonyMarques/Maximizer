import cvxpy as cp

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
    if len(constants) == 1:
        print("<!> Você definiu %i produto, cuja quantidade é representada por "%(len(constants)), end="")
    else:
        print("<!> Você definiu %i produtos, cujas quantidades são representadas por "%(len(constants)), end="")
    for i in range(1, len(constants)+1):
        if i == len(constants) and len(constants) == 1:
            print("x%i! "%(i))
            products.append("p%i"%(i))
        elif i == 1:
            print("x%i"%(i), end="")
            products.append("p%i"%(i))
        elif i == len(constants):
            print(" e x%i! "%(i))
            products.append("p%i"%(i))
        else:
            print(", x%i"%(i), end="")
            products.append("p%i"%(i))

    for i in range(1, len(constants)+1):
        if i == len(constants):
            objective += str(constants[i-1]) + "x%i" %(i)
        else:
            objective += str(constants[i-1]) + "x%i + " %(i)

    print("\n<?> z = %s corresponde à função objetivo? S/N?" %(objective))

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
    """print("<?> Restrição de %s gerada para %i produto(s)"%(name, len(constants)-1), end="")
    for i in range(1, len(constants)):
        if i == len(constants)-1:
            print(" e x%i. "%(i))
        else:
            print(", x%i"%(i), end="")"""

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
    constraint = "%s %s " %(constant.replace("p", "x"), mark) + str(value)
    if mark == "<=":
        #print("\n<?> Restrição de quantidade máxima gerada para 1 produto, %s."%(constant))
        print("\n<?> %s representa a restrição de quantidade máxima do produto %s? S/N?" %(constraint, constant))
    else:
        #print("\n<?> Restrição de quantidade mínima gerada para 1 produto, %s."%(constant))
        print("\n<?> %s representa a restrição de quantidade mínima do produto %s? S/N?" %(constraint, constant))
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

def objective_costs(messages):
    while True:
        result = input_costs(messages[8])
        if result == 0:
            print("<!> Vamos tentar de novo!\n")
            continue
        break
    return result

def objective(messages, results):
    print(messages[0],"\n")
    constants = objective_costs(messages)
    if len(results) == 0:
        while True:
            result = confirm_objective(constants)
            if result == 0:
                constants = objective_costs(messages)
                continue
            variables, constants = list(), list()
            for i in result[0]:
                constant = cp.Parameter()
                constant.value = i
                constants.append(constant)
                variables.append(cp.Variable(integer=True))
            results.extend([constants, variables, result[1]])
            break
        return result[2]
    else:
        while True:
            if (len(constants) != len(results[0])):
                print("<!> Este problema foi inicialmente definido com "+str(len(results[0]))+" produto(s). Por favor, entre com o(s) lucro(s) correspondente(s) a esse(s) produto(s).")
                constants = objective_costs(messages)
                continue
            result = confirm_objective(constants)
            if result == 0:
                constants = objective_costs(messages)
                continue
            for i in range(len(result[0])):
                results[0][i].value = result[0][i]
            break
        return result[2]

def constraint_costs(message, defined_constants):
    while True:
        result = input_costs(message)
        if ((not result) or len(result) != len(defined_constants)+1):
            print("<!> Vamos tentar de novo!\n")
            continue
        break
    return result

def basic_constraint(message, name, results, constraints, mark):
    print("<!> Vamos à restrição de %s.\n"%name)
    constants = constraint_costs(message, results[0])
    while True:
        result = confirm_constraint(constants, name, mark)
        if result == 0:
            constants = constraint_costs("<!> Vamos tentar definir a restrição de %s de novo! " %name, results[0])
            continue
        for i in range(len(constants)):
            if i == 0:
                constraint = constants[i]*results[1][i]
            elif i == len(constants)-1:
                if mark == ">=":
                    constraint = (constraint >= constants[i])
                elif mark == "<=":
                    constraint = (constraint <= constants[i])
                elif mark == "==":
                    constraint = (constraint == constants[i])
            else:
                constraint += constants[i]*results[1][i]
        constraints.append(constraint)
        break
    return result

def constraint_value(message, selected_constant):
    while True:
        result = input_constraints(message, selected_constant)
        if not result:
            print("<!> Vamos tentar de novo!\n")
            continue
        break
    return result

def value_constraint(messages, errors, name, results, constraints, mark, string_answers=None):
    print("<!> Vamos à restrição de %s.\n"%name)
    string_constraints = []

    if string_answers:
        if mark == ">=" and len(string_answers) > 6 and string_answers[6][0].find(">=")>=0:
            del constraints[6:6+len(string_answers[6])]
            print(constraints)
        elif mark == "<=" and len(string_answers) > 6 and (string_answers[6][0].find("<=")>=0 or (len(string_answers) > 7 and string_answers[7][0].find("<=")>=0)):
            if string_answers[6][0].find("<=")>=0:
                del constraints[5:]
            else:
                del constraints[5+len(string_answers[6]):]

    while True:
        selected_constants = input(messages[0])
        print()
        should_restart = False
        if len(selected_constants) != 0:
            selected_constants = selected_constants.split(",")
            for i in range(0, len(selected_constants)):
                selected_constants[i] = selected_constants[i].strip()
                if selected_constants[i] not in results[2]:
                    print(errors[0] + selected_constants[i] + "!")
                    should_restart = True
                    break

            if should_restart:
                continue

            for i in selected_constants:
                while True:
                    value = constraint_value(messages[1], i)
                    result = confirm_value_constraint(i,value, mark)
                    if (result):
                        string_constraints.append(result)
                        if mark == ">=":
                            if string_answers:
                                constraints[6:6] = [results[1][results[2].index(i)] >= value]
                            else:
                                constraints.append(results[1][results[2].index(i)] >= value)
                            break
                        elif mark == "<=":
                            constraints.append(results[1][results[2].index(i)] <= value)
                            break
                        elif mark == "==":
                            constraints.append(results[1][results[2].index(i)] == value)
                            break
                    continue
            return string_constraints
        else:
            should_restart = confirm_skip()
            if should_restart:
                continue
            return []
        break

def new_investiments_problem(string_answers, results, operator):
    invConstraint = string_answers[1][:].split("= ")
    invConstraint[0] = invConstraint[0][:-1]
    if operator == "d":
        invConstraint[1] = float(invConstraint[1])*2
    elif operator == "h":
        invConstraint[1] = float(invConstraint[1])/2
    invConstraint[0] = invConstraint[0].split("+")
    for i in range(len(invConstraint[0])):
        invConstraint[0][i] = float(invConstraint[0][i].replace("x%d"%(i+1),"").strip())

    newInvConstraint = invConstraint[0][0] * results[1][0] 
    for i in range(1,len(invConstraint[0])):
        newInvConstraint += invConstraint[0][i] * results[1][i]
    return (newInvConstraint <= invConstraint[1], invConstraint[1])

def write_objective(results):
    objetivo = results[0][0]*results[1][0]
    for i in range(1,len(results[0])):
        objetivo += results[0][i]*results[1][i]
    return objetivo

def write_result(variables, str_constraints):
    newStr_constraints = str_constraints[0].split("+")
    print("<!> ", end="")
    for i in range(len(variables)):
        if i == len(variables)-1:
            print(" e x%d = %s."%(i+1,str(variables[i])), end="")
        elif i == len(variables)-2:
            print("x%d = %s"%(i+1,str(variables[i])), end="")
        else:
            print("x%d = %s, "%(i+1,str(variables[i])), end="")
        newStr_constraints[i] = newStr_constraints[i].replace("x%d"%(i+1)," * "+str(variables[i]))
    print()
    return "+".join(newStr_constraints)

def calc_result(objetivo, constraints, string_answers, results):
    problema = cp.Problem(cp.Maximize(objetivo), constraints)
    #problema.solve(solver=cp.CPLEX)
    problema.solve()

    print("*-*"*15)
    print("\n<!> Função objetivo do problema: z = %s."%(string_answers[0]))
    print("<!> Restrições definidas:\n")
    count = 0

    print(string_answers)
    for i in range(len(string_answers)):
        if i == 0:
            continue
        else:
            if (type(string_answers[i]) == list):
                for x in string_answers[i]:
                    print(x.replace("p","x"))
                    count += 1
            else:
                print(string_answers[i].replace("p","x"))
                count += 1

    print("\n<!> Há", count, "restrições.")

    print()

    try:
        if (int(problema.value)):
            print("<!> Solução ótima para o problema definido:")
            newStr_constraints = write_result(list(map(lambda x: x.value,results[1])),string_answers)
            print("<!> Aplicando esses valores na função objetivo, temos:")
            print("<!> %d = "%(int(problema.value)), end="")
            print(newStr_constraints+'\n')
    except:
        print("<!> Não há solução ótima para o problema definido!")

    try:
        newInvConstraint = new_investiments_problem(string_answers, results, "d")#double
        constraints2 = constraints.copy()
        constraints2[0] = newInvConstraint[0]
        problema = cp.Problem(cp.Maximize(objetivo), constraints2)
        #problema.solve(solver=cp.CPLEX)
        problema.solve()

        if (int(problema.value)):
            print("<!> Solução ótima para um problema com o dobro do investimento (%.1f):"%(newInvConstraint[1]))
            newStr_constraints = write_result(list(map(lambda x: x.value,results[1])),string_answers)
            print("<!> Aplicando esses valores na função objetivo, temos:")
            print("<!> %d = "%(int(problema.value)),end="")
            print(newStr_constraints+'\n')
    except:
        pass

    try:
        newInvConstraint = new_investiments_problem(string_answers, results, "h")#half
        constraints3 = constraints.copy()
        constraints3[0] = newInvConstraint[0]
        problema = cp.Problem(cp.Maximize(objetivo), constraints3)
        #problema.solve(solver=cp.CPLEX)
        problema.solve()

        if (int(problema.value)):
            print("<!> Solução ótima para um problema com a metade do investimento (%.1f):"%(newInvConstraint[1]))
            newStr_constraints = write_result(list(map(lambda x: x.value,results[1])),string_answers)
            print("<!> Aplicando esses valores na função objetivo, temos:")
            print("<!> %d = "%(int(problema.value)),end="")
            print(newStr_constraints+'\n')
    except:
        pass