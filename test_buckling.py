import numpy as np
from scipy import optimize

def column_stress_error(P, L, E, A, rho, c, e, sigma_allow):
    # פרמטרים לדוגמה #
    #A, E, L, rho, e, c = 5000, 200000, 3000, 50, 20, 100
    # נוסחת הסקנט #
    sec_term = 1 / np.cos((L / (2 * rho)) * np.sqrt(P / (E * A)))
    sigma_max = (P / A) * (1 + (e * c / rho**2) * sec_term)
    return sigma_max - sigma_allow

def find_critical_load(L, E, A, rho, c, e, sigma_allow):
    # חישוב עומס אוילר התיאורטי עם rho #
    P_euler = (np.pi**2 * E * (A * rho**2)) / L**2
    
    # ניחוש ראשוני דינמי ובטוח #
    guess = P_euler * 0.4
    
    P_critical = optimize.newton(lambda P: column_stress_error(P, L, E, A, rho, c, e, sigma_allow), guess)
    return P_critical
