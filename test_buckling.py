import numpy as np
from scipy import optimize

def column_stress_error(P, L, E, A, r, c, e, sigma_allow):
    P = max(P, 0.0)
    arg = (L/(2*r)) * np.sqrt(P/(E*A))
    if np.isnan(arg) or np.isinf(arg):
        return 1e6
    cosv = np.cos(arg)
    if abs(cosv) < 1e-12:
        return 1e6
    sec_term = 1.0 / cosv
    sigma_max = (P/A) * (1 + (e*c/r**2) * sec_term)
    return sigma_max - sigma_allow

def find_critical_load(L, E, A, r, c, e, sigma_allow):
    # מציאת ברקטה (a,b)
    a, b = 0.0, 1.0
    while column_stress_error(b, L, E, A, r, c, e, sigma_allow) < 0:
        b *= 2.0
        if b > 1e12:
            raise RuntimeError("Could not bracket root")
    P_critical = optimize.brentq(lambda P: column_stress_error(P, L, E, A, r, c, e, sigma_allow), a, b)
    return P_critical
