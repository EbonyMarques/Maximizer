from domain.problem import Problem
from domain.solver import Solver

problem = Problem()

"""
max z = 2x + 3y + 2z
2x + y + z <= 4
x + 2y + z <= 7
z          <= 5
x, y, z    >= 0
"""

solver = Solver([-2, -3, -2])
solver.add_constraint([2, 1, 1], 4)
solver.add_constraint([1, 2, 1], 7)
solver.add_constraint([0, 0, 1], 5)
solver.solve()

#optimal_solution = Solver()
#problem.add_solution(optimal_solution)