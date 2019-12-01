import cvxpy as cp
from domain.problem import Problem
from domain.structure import *

results = []
constraints = []
names = ["Investimento", "Espaço", "Quantidade mínima de produto", "Quantidade máxima de produto"]
messages = ["<!> Vamos começar setando a função objetivo do problema!",
            ">>> Para cada produto considerado, entre com seu custo: ",
            "<!> Ótimo. Agora, setemos as restrições!",
            ">>> Para cada produto considerado, entre com sua área: ",
            "<!> Caso queira adicionar restrições de quantidades mínimas, entre com aqueles\n<!>produtos que terão. Por exemplo: x1,x4,x10...\n<!> Caso não queira, apenas tecle enter para continuar. ", 
            "<!> Caso queira adicionar restrições de quantidades máximas, entre com aqueles\n<!>produtos que terão. Por exemplo: x1,x4,x10...\n<!> Caso não queira, apenas tecle enter para continuar. ",
            ">>> Entre com a quantidade mínima do produto ",
            ">>> Entre com a quantidade máxima do produto ",
            ">>> "]
errors = ["<!> Este produto não existe: "]

while True:
    print(messages[0]+"\n")
    result = input_objective(messages[1])
    if result == 0:
        messages[0] = "<!> Vamos tentar de novo!"
        continue
    constants = result
    while True:
        result = confirm_objective(constants)
        if result == 0:
            continue
        variables = list()
        constants = list()
        for i in result[0]:
            constant = cp.Parameter()
            constant.value = i
            variables.append(cp.Variable())
            constants.append(constant)
        results.append(constants)
        results.append(variables)
        results.append(result[1])
        break
    break

print("\n",results)
print(messages[2])

while True:
    result = set_constraint(names[0], messages[1], results[0])
    print(result)
    if result == 0:
        messages[1] = "<!> Vamos tentar setar a restrição de %s de novo." %names[0]
        continue
    for i in range(len(result)):
        if i == 0:
            constraint = result[i]*results[1][i]
        elif i == len(result)-1:
            constraint = (constraint <= result[i])
        else:
            constraint += result[i]*results[1][i]
    constraints.append(constraint)
    break

# print(results)

while True:
    result = set_constraint(names[1], messages[3], results[0])
    if result == 0:
        messages[1] = "<!> Vamos tentar setar a restrição de %s de novo." %names[1]
        continue
    for i in range(len(result)):
        if i == 0:
            constraint = result[i]*results[1][i]
        elif i == len(result)-1:
            constraint = (constraint <= result[i])
        else:
            constraint += result[i]*results[1][i]
    constraints.append(constraint)
    break

#print(results)

for i in range(len(results[0])):
    constraints.append(results[1][i] >= 0)

while True:
    a = input("\n"+messages[4])
    c = True
    if len(a) != 0:
        b = a.split(",")
        for i in range(0, len(b)):
            b[i] = b[i].strip()
        for i in b:
            if i not in results[2]:
                print("\n"+errors[0] + i + "!")
                c = False
                break
            result = set_constraint_2(messages[6], results[2], i)
            constraints.append(results[1][results[2].index(i)] >= result)
        if not c:
            continue
    break

# #print(results)
# #print(constraints)

while True:
    a = input("\n"+messages[5])
    c = True
    if len(a) != 0:
        b = a.split(",")
        for i in range(0, len(b)):
            b[i] = b[i].strip()
        for i in b:
            if i not in results[2]:
                print("\n"+errors[0] + i + "!")
                c = False
                break
            result = set_constraint_2(messages[7], results[2], i)
            constraints.append(results[1][results[2].index(i)] <= result)
        if not c:
            continue
    break

for i in range(len(results[0])):
        if i == 0:
            objetivo = results[0][i]*results[1][i]
        else:
            objetivo += results[0][i]*results[1][i]

problema = cp.Problem(cp.Maximize(objetivo), constraints)
problema.solve()

print("\n<!> Há", len(constraints), "restrições.\n")

print(problema.value, list(map((lambda x: x.value),results[1])), problema.status)