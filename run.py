import cvxpy as cp
from domain.problem import Problem
from domain.structure import *
from domain.main import *

#Results Guide
#[0] - Constants([cp.Parameter(), cp.Parameter(), cp.Parameter()])
#[1] - Variables([cp.Variable(), cp.Variable(), cp.Variable()])
#[2] - Strigs(["x1","x2","x3"])

results = []
constraints = []
string_answers=[]
names = ["Investimento", "Espaço", "Quantidade mínima de produto", "Quantidade máxima de produto"]
messages = ["<!> Vamos começar definindo a função objetivo do problema!",
            ">>> Para cada produto considerado, entre com seu custo e, por fim, com o montante disponível para Investimento: ",
            "<!> Ótimo. Agora, definiremos as restrições!",
            ">>> Para cada produto considerado, entre com sua área e, por fim, com a área total disponível: ",
            "<!> Caso queira adicionar restrições de quantidades mínimas, entre com aqueles produtos que terão. Por exemplo: x1,x2,...\n<!> Caso não queira, apenas tecle enter para continuar.", 
            "<!> Caso queira adicionar restrições de quantidades máximas, entre com aqueles produtos que terão. Por exemplo: x1,x2,...\n<!> Caso não queira, apenas tecle enter para continuar.",
            ">>> Entre com a quantidade mínima do produto ",
            ">>> Entre com a quantidade máxima do produto ",
            ">>> Para cada produto considerado, entre com seu lucro: ",
            ">>> "]
errors = ["<!> Este produto não existe: "]

# Definição da função objetivo
string_answers.append(
    objective(messages, results)
)

print(messages[2])

# Definição da restrição de investimento
string_answers.append(
    basic_constraint(messages[1], names[0], results, constraints, "<=")
)

#Definição da restrição de espaço
string_answers.append(
    basic_constraint(messages[3], names[1], results, constraints, "<=")
)

#Definição da restrição de valores positivos ">=0"
for i in range(len(results[0])):
    constraints.append(results[1][i] >= 0)
    string_answers.append(results[2][i]+" >= 0")

#Definição da restrição de quantidades mínimas
constraint = value_constraint([messages[4], messages[6], messages[-1]], errors, names[2], results, constraints, ">=")
if (constraint):
    string_answers.append(constraint)

#Definição da restrição de quantidades máximas
constraint = value_constraint([messages[5], messages[7], messages[-1]], errors, names[3], results, constraints, "<=")
if (constraint):
    string_answers.append(constraint)

#Construção da função Objetivo c1*x1+c2*x2+...+cn*xn
objetivo = results[0][0]*results[1][0]
for i in range(1,len(results[0])):
    objetivo += results[0][i]*results[1][i]

#Construção e resolução do problema de maximização, utilizando a biblioteca solver
problema = cp.Problem(cp.Maximize(objetivo), constraints)
problema.solve()

print("<!> Há", len(constraints), "restrições.\n")
for i in constraints:
    print(i)
print()
print(string_answers)

print(problema.value, list(map(lambda x: x.value,results[1])), problema.status)

#(1*47)+(2*18)+(3*39)
#(10*47)+(20*18)+(30*39)
#(0,5*47)+(1*18)+(1*39)