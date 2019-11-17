#from solution import Solution
import numpy as np

class Solver():
    def next_round_r(self, table):    
        m = min(table[:-1,-1])    
        if m>= 0:        
            return False    
        else:        
            return True

    def next_round(self, table):    
        lr = len(table[:,0])   
        m = min(table[lr-1,:-1])    
        if m>=0:
            return False
        else:
            return True
        
    def find_neg_r(self, table):
        lc = len(table[0,:])
        m = min(table[:-1,lc-1])
        if m<=0:        
            n = np.where(table[:-1,lc-1] == m)[0][0]
        else:
            n = None
        return n

    def find_neg(self, table):
        lr = len(table[:,0])
        m = min(table[lr-1,:-1])
        if m<=0:
            n = np.where(table[lr-1,:-1] == m)[0][0]
        else:
            n = None
        return n

    def loc_piv_r(self, table):
        total = []        
        r = self.find_neg_r(table)
        row = table[r,:-1]
        m = min(row)
        c = np.where(row == m)[0][0]
        col = table[:-1,c]
        for i, b in zip(col,table[:-1,-1]):
            if i**2>0 and b/i>0:
                total.append(b/i)
            else:                
                total.append(10000)
        index = total.index(min(total))        
        return [index,c]

    def loc_piv(self, table):
        if self.next_round(table):
            total = []
            n = self.find_neg(table)
            for i,b in zip(table[:-1,n],table[:-1,-1]):
                if b/i >0 and i**2>0:
                    total.append(b/i)
                else:
                    total.append(10000)
            index = total.index(min(total))
            return [index,n]

    def pivot(self, row,col,table):
        lr = len(table[:,0])
        lc = len(table[0,:])
        t = np.zeros((lr,lc))
        pr = table[row,:]
        if table[row,col]**2>0:
            e = 1/table[row,col]
            r = pr*e
            for i in range(len(table[:,col])):
                k = table[i,:]
                c = table[i,col]
                if list(k) == list(pr):
                    continue
                else:
                    t[i,:] = list(k-r*c)
            t[row,:] = list(r)
            return t
        else:
            print('Cannot pivot on this element.')

    def convert_min(self, table):
        table[-1,:-2] = [-1*i for i in table[-1,:-2]]
        table[-1,-1] = -1*table[-1,-1]    
        return table

    def gen_var(self, table):
        lc = len(table[0,:])
        lr = len(table[:,0])
        var = lc - lr -1
        v = []
        for i in range(var):
            v.append('x'+str(i+1))
        return v

    def maxz(self, table):
        while self.next_round_r(table)==True:
            table = self.pivot(self.loc_piv_r(table)[0],self.loc_piv_r(table)[1],table)
        while self.next_round(table)==True:
            table = self.pivot(self.loc_piv(table)[0],self.loc_piv(table)[1],table)        
        lc = len(table[0,:])
        lr = len(table[:,0])
        var = lc - lr -1
        i = 0
        val = {}
        for i in range(var):
            col = table[:,i]
            s = sum(col)
            m = max(col)
            if float(s) == float(m):
                loc = np.where(col == m)[0][0]            
                val[self.gen_var(table)[i]] = table[loc,-1]
            else:
                val[self.gen_var(table)[i]] = 0
        val['max'] = table[-1,-1]
        return val

    def minz(self, table):
        table = self.convert_min(table)
        while self.next_round_r(table)==True:
            table = self.pivot(self.loc_piv_r(table)[0],self.loc_piv_r(table)[1],table)    
        while self.next_round(table)==True:
            table = self.pivot(self.loc_piv(table)[0],self.loc_piv(table)[1],table)       
        lc = len(table[0,:])
        lr = len(table[:,0])
        var = lc - lr -1
        i = 0
        val = {}
        for i in range(var):
            col = table[:,i]
            s = sum(col)
            m = max(col)
            if float(s) == float(m):
                loc = np.where(col == m)[0][0]             
                val[self.gen_var(table)[i]] = table[loc,-1]
            else:
                val[self.gen_var(table)[i]] = 0 
                val['min'] = table[-1,-1]*-1
        return val

    def solve(self, problem):
        result = self.maxz(problem.table)
        return result