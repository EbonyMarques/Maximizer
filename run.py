from domain.problem import Problem
from domain.solver import Solver
from domain.constraint import Constraint
from domain.structure import set_objective, set_constraint, set_constraint_2

constraints = [["investimento", ]]
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
        results.append(result[0])
        results.append(result[2])
        break

#print(results)
print()

constraint1 = Constraint("Investimento", [">>> Considerando a ordem dos produtos setados, entre com os custos individuais de cada um: ", "", ">>> Qual é o valor total disponível para investimento? "], ["<!> A quantidade de custos difere da quantidade de produtos anteriormente setados.", "", "<!> Esse valor deve ser inteiro ou decimal!"])
print(messages[1])
while True:
    result = set_constraint(constraint1, results[0])
    if result == 0:
        print("\n"+constraint1.error1)
        messages[1] = "<!> Vamos tentar setar a restrição de %s de novo." %constraint1.name
        continue
    constraints.append(result)
    break

#print(results)

constraint2 = Constraint("Espaço", [">>> Considerando a ordem dos produtos setados, entre com a área ocupada por cada um: ", "", ">>> Qual é a área total disponível no estoque? "], ["<!> A quantidade de custos difere da quantidade de produtos anteriormente setados.", "", "<!> Esse valor deve ser inteiro ou decimal!"])
while True:
    result = set_constraint(constraint2, results[0])
    if result == 0:
        print("\n"+constraint2.error1)
        messages[1] = "<!> Vamos tentar setar a restrição de %s de novo." %constraint1.name
        continue
    constraints.append(result)
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
            if i not in results[1]:
                print("\n"+errors[0] + i + "!")
                c = False
                break
            result = set_constraint_2(constraint3, results[1], i, "G")
            constraints.append(result)
        if not c:
            continue
    break

#print(results)
#print(constraints)

constraint4 = Constraint("Quantidade máxima", [">>> Entre com a quantidade máxima do produto ", "", ""], ["<!> Esse valor deve ser inteiro ou decimal!", "", ""])
while True:
    a = input("\n"+messages[3])
    c = True
    if len(a) != 0:
        b = a.split(",")
        for i in range(0, len(b)):
            b[i] = b[i].strip()
        for i in b:
            if i not in results[1]:
                print("\n"+errors[0] + i + "!")
                c = False
                break
            result = set_constraint_2(constraint4, results[1], i, "L")
            constraints.append(result)
        if not c:
            continue
    break

for i in constraints:
    print(i)

objective = ""

for i in results[0]:
    objective += str(i) + ","

objective = objective[:-1]
print(objective)

problem = Problem(len(results[0]),len(constraints))

for i in constraints:
    problem.constrain(i)

problem.obj(objective)
"""
problem = Problem(3,7)
problem.constrain('200,20,15,L,3000.0')
problem.constrain('0.5,0.2,0.3,L,30.0')
#problem.constrain('1,1,1,L,150.0')
problem.constrain('1,0,0,G,10.0')
problem.constrain('0,1,0,G,10.0')
problem.constrain('0,0,1,G,10.0')
problem.constrain('0,1,0,L,100.0')
problem.constrain('0,0,1,L,50.0')
problem.obj('35,22,10')
print(Solver().solve(problem))
"""

print(Solver().solve(problem))