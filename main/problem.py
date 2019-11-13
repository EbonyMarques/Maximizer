class Problem():
    def __init__(self):
        self.__objective = []
        self.__variables = []
        self.__constraints = []
        self.__restrictions = []
        self.__solutions = []

    ax1,bx2,cx3...,mxn
    self.__objective.sum

    def set_objective(self):
        for i in range(0, len(self.__variables)):
            self.__objective.append(self.__variables[i]*self.__constraints[i])
    
    def get_objective(self):
        return self.__objective

    def add_objective_term(self, variable, constraint):
        self.__variables.append(variable)
        self.__constraints.append(constraint)
        self.set_objective()

    def add_restriction(self, restriction):
        self.__restrictions.append(restriction)
    
    def get_restrictions(self):
        return self.__restrictions

    def add_solution(self, solution):
        self.__solutions.append(solution)

    