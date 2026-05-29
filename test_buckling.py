import numpy as np
from scipy import optimize
def column_stress_error(P,L,E,A,r,c,e,sigma_allow):
    #פרמטרים לדוגמא
    #A,E,L,r,e,c =5000,200000,3000,50,20,100
    #נוסחאת הסקנט
    sec_term = 1 / np.cos((L/(2*r)) * np.sqrt(P/(E*A)))
    sigma_max - sigma_allow

def find_critical_load(L,E,A,r,c,e, sigma_allow):
  p_critical = optimize.newton(lambda P: column_stress_error(P,I,E,A,r,c,e, sigma_allow),500000)    
  return p_critical
