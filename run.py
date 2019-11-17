from domain.problem import Problem
from domain.solver import Solver

objective_raw = input(">>> Entre com as constantes da função objetivo: ")
constants = objective_raw.split(",")
objective = ""
for i in range(0, len(constants)):
    if i == len(constants)-1:
        objective += constants[i] + "x%s" %(i)
    else:
        objective += constants[i] + "x%s + " %(i)
print("<?> %s é a função objetivo? " %(objective))

"""
variables = int(input(">>> Entre com a quantidade de variáveis: "))
constants = []

for i in range(0, variables):
    constants.append(int(input(">>> Entre com o lucro da %ia variável: " %(i+1))))
"""
"""problem = Problem(3,6)
problem.constrain('200,20,15,L,5000')
problem.constrain('0.5,0.2,0.3,L,30')
problem.constrain('1,1,1,L,150')
problem.constrain('1,0,0,G,10')
problem.constrain('0,1,0,G,10')
problem.constrain('0,0,1,G,10')
problem.obj('35,22,10')
print(Solver().solve(problem))"""