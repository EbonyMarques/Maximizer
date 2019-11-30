import cvxpy as cp

x1 = cp.Variable()
c1 = cp.Parameter()
x2 = cp.Variable()
c2 = cp.Parameter()
x3 = cp.Variable()
c3 = cp.Parameter()
c1.value = 1
c2.value = 2
c3.value = 3

constraints = [
    10*x1 + 20*x2 + 30*x3 <= 4000, 
    0.5*x1 + 1*x2 + 1*x3 <= 2000, 
    x1 >= 10,
    x3 >= 10,
    x1 <= 100,
    x3 <= 50
]

# DCP problems.
prob1 = cp.Problem(cp.Maximize(c1*x1 + c2*x2 + c3*x3),
                    constraints)
# prob2 = cp.Problem(cp.Maximize(cp.sqrt(x - y)),
#                 [2*x - 3 == y,
#                  cp.square(x) <= 2])

prob1.solve()

print("prob1 is DCP:", prob1.value, x1.value, x2.value, x3.value, prob1.status)