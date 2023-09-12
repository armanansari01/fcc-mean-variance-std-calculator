import numpy as np

def calculate(list):
  myarr = np.array(list).reshape(3,3)
  calculation = {
    'mean': None,
    'variance':None,
    'standard deviation':None,
    'max':None,
    'min':None,
    'sum':None
  }
  if len(list) != 9:
    print("List must contain nine numbers.")
  else:
    print(myarr)
    meanlist = [np.mean(myarr,axis=0),np.mean(myarr,axis=1),np.mean(myarr)]
    varlist = [np.var(myarr,axis=0),np.var(myarr,axis=1),np.var(myarr)]
    stdlist = [np.std(myarr,axis=0),np.std(myarr,axis=1),np.std(myarr)]
    maxlist = [np.max(myarr,axis=0),np.max(myarr,axis=1),np.max(myarr)]
    minlist = [np.min(myarr,axis=0),np.min(myarr,axis=1),np.min(myarr)]
    sumlist = [np.sum(myarr,axis=0),np.sum(myarr,axis=1),np.sum(myarr)]
    
    calculation['mean'] = meanlist  
    calculation['variance']= varlist
    calculation['standard deviation']= stdlist
    calculation['max'] = maxlist
    calculation['min'] = minlist
    calculation['sum'] = sumlist 
    return calculation
