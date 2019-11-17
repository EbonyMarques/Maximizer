import numpy as np

class Problem():
    def __init__(self, a, b):
        self.table = self.gen_matrix(a, b)
        
    def gen_matrix(self, var,cons):
        tab = np.zeros((cons+1, var+cons+2))    
        return tab

    def convert(self, eq):
        eq = eq.split(',')
        if 'G' in eq:
            g = eq.index('G')
            del eq[g]
            eq = [float(i)*-1 for i in eq]
            return eq
        if 'L' in eq:
            l = eq.index('L')
            del eq[l]
            eq = [float(i) for i in eq]
            return eq

    def add_cons(self, table):
        lr = len(table[:,0])
        empty = []
        for i in range(lr):
            total = 0
            for j in table[i,:]:                       
                total += j**2
            if total == 0: 
                empty.append(total)
        if len(empty)>1:
            return True
        else:
            return False

    def constrain(self,eq):
        if self.add_cons(self.table) == True:
            lc = len(self.table[0,:])
            lr = len(self.table[:,0])
            var = lc - lr -1      
            j = 0
            while j < lr:            
                row_check = self.table[j,:]
                total = 0
                for i in row_check:
                    total += float(i**2)
                if total == 0:                
                    row = row_check
                    break
                j +=1
            eq = self.convert(eq)
            i = 0
            while i<len(eq)-1:
                row[i] = eq[i]
                i +=1        
            row[-1] = eq[-1]
            row[var+j] = 1    
        else:
            print('Cannot add another constraint.')

    def add_obj(self, table):
        lr = len(table[:,0])
        empty = []
        for i in range(lr):
            total = 0        
            for j in table[i,:]:
                total += j**2
            if total == 0:
                empty.append(total)    
        if len(empty)==1:
            return True
        else:
            return False

    def obj(self,eq):
        if self.add_obj(self.table)==True:
            eq = [float(i) for i in eq.split(',')]
            lr = len(self.table[:,0])
            row = self.table[lr-1,:]
            i = 0        
            while i<len(eq)-1:
                row[i] = eq[i]*-1
                i +=1
            row[-2] = 1
            row[-1] = eq[-1]
        else:
            print('You must finish adding constraints before the objective function can be added.')

