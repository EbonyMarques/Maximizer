import cvxpy as cp
from .structure import *

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

def value_constraint(messages, errors, name, results, constraints, mark):
    print("<!> Vamos à restrição de %s.\n"%name)
    string_constraints = []

    while True:
        print(messages[0])
        selected_constants = input(messages[2])
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
                    string_constraints.append(result)
                    if (result):
                        if mark == ">=":
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
        break