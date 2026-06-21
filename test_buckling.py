import numpy as np
from scipy import optimize

def column_stress_error(P, L, E, A, r, c, e, sigma_allow):
    # מניעת ערכים שליליים בתוך השורש בזמן החיפוש של ניוטון
    if P <= 0:
        return -sigma_allow
        
    # נוסחת הסקנט המתוקנת עם סוגריים תקינים #
    sec_term = 1 / np.cos(((L / (2 * r)) * np.sqrt(P / (E * A))))
    sigma_max = (P / A) * (1 + (e * c / r**2) * sec_term)
    return sigma_max - sigma_allow

def find_critical_load(L, E, A, r, c, e, sigma_allow):
    # ניחוש ראשוני יציב של 1000.0 מונע Overflow
    P_critical = optimize.newton(lambda P: column_stress_error(P, L, E, A, r, c, e, sigma_allow), 1000.0)
    return P_critical

if __name__ == "__main__":
    A = 5000
    E = 200000
    L = 3000
    r = 50
    e = 20
    c = 100
    sigma_allow = 100
    
    try:
        p_crit = find_critical_load(L, E, A, r, c, e, sigma_allow)
        print(f"P_critical: {p_crit:.2f}")
    except Exception as err:
        print(f"Error: {err}")
