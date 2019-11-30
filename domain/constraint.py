class Constraint():
    def __init__(self, name, messages, errors):
        self.name = name
        self.message1 = messages[0]
        self.message2 = messages[1]
        self.message3 = messages[2]
        self.error1 = errors[0]
        self.error2 = errors[1]
        self.error3 = errors[2]
        self.constraint = None

    def set_constraint(self, constraint):
        self.constraint = constraint