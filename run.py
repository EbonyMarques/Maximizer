import cvxpy as cp
from domain.problem import Problem
from domain.solver import Solver
from domain.constraint import Constraint
from domain.structure import set_objective, set_constraint, set_constraint_2

results = []
constraints = []
messages = ["<!> É hora de setar a função objetivo!", "<!> Ótimo. Comecemos a setar as restrições!", "<?> Você deseja inserir restrições de quantidades mínimas para os produtos?\n<?> Caso queira, entre com os produtos que terão as restrições. Por exemplo: x1,x4,x10...\nCaso não queira, tecle enter: ", "<?> Você deseja inserir restrições de quantidades máximas para os produtos?\n<?> Caso queira, entre com os produtos que terão as restrições. Por exemplo: x1,x4,x10...\nCaso não queira, tecle enter: "]
errors = ["<!> Este produto não existe: "]

while True:
    result = set_objective(messages[0])
    if result == 0:
        messages[0] = "\n<!> Vamos tentar de novo!"
        continue
    else:
        variables = list()
        constants = list()
        for i in result[0]:
            c = cp.Parameter()
            c.value = i
            variables.append(cp.Variable())
            constants.append(c)
        results.append(constants)
        results.append(variables)
        results.append(result[2])

        break

# print(results)
print()

constraint1 = Constraint("Investimento", [">>> Considerando a ordem dos produtos setados, entre com os custos individuais de cada um: ", "", ">>> Qual é o valor total disponível para investimento? "], ["<!> A quantidade de custos difere da quantidade de produtos anteriormente setados.", "", "<!> Esse valor deve ser inteiro ou decimal!"])
print(messages[1])
while True:
    result = set_constraint(constraint1, results[0])
    print(result)
    if result == 0:
        print("\n"+constraint1.error1)
        messages[1] = "<!> Vamos tentar setar a restrição de %s de novo." %constraint1.name
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

constraint2 = Constraint("Espaço", [">>> Considerando a ordem dos produtos setados, entre com a área ocupada por cada um: ", "", ">>> Qual é a área total disponível no estoque? "], ["<!> A quantidade de custos difere da quantidade de produtos anteriormente setados.", "", "<!> Esse valor deve ser inteiro ou decimal!"])
while True:
    result = set_constraint(constraint2, results[0])
    if result == 0:
        print("\n"+constraint2.error1)
        messages[1] = "<!> Vamos tentar setar a restrição de %s de novo." %constraint1.name
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

constraint3 = Constraint("Quantidade mínima", [">>> Entre com a quantidade mínima do produto ", "", ""], ["<!> Esse valor deve ser inteiro ou decimal!", "", ""])
while True:
    a = input("\n"+messages[2])
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
            result = set_constraint_2(constraint3, results[2], i)
            constraints.append(results[1][results[2].index(i)] >= result)
        if not c:
            continue
    break

# #print(results)
# #print(constraints)

constraint4 = Constraint("Quantidade máxima", [">>> Entre com a quantidade máxima do produto ", "", ""], ["<!> Esse valor deve ser inteiro ou decimal!", "", ""])
while True:
    a = input("\n"+messages[3])
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
            result = set_constraint_2(constraint4, results[2], i)
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

print(problema.value, list(map((lambda x: x.value),results[1])), problema.status)