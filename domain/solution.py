class Solution():
    def __init__(self):
        self.__variables_quantities = {}
        self.__objective_result = None
        self.__restrictions_results = {}

    def add_variable_quantity(self, variable, quantity):
        self.__variables_quantities[variable] = quantity
    
    def get_variables_quantities(self):
        return self.__variables_quantities
    
    def set_objective_result(self, value):
        self.__objective_result = value
    
    def get_objective_result(self):
        return self.__objective_result

    def add_restriction_result(self, restriction, value):
        self.__restrictions_results[restriction] = value

    def get__restrictions_results(self):
        return self.__restrictions_results