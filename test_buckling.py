import numpy as np
from scipy import optimize

def column_stress_error(P, L, E, A, r, c, e, sigma_allow):

    if P <= 0:
        return np.inf

    theta = (L/(2*r)) * np.sqrt(P/(E*A))
    sec_term = 1 / np.cos(theta)

    sigma_max = (P/A) * (1 + (e*c/r**2) * sec_term)

    return sigma_max - sigma_allow


def find_critical_load(L, E, A, r, c, e, sigma_allow):

    return optimize.newton(
        lambda P: column_stress_error(
            P, L, E, A, r, c, e, sigma_allow
        ),
        x0=500000
    )
