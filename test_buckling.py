import numpy as np
from scipy import optimize

def column_stress_error(P, L, E, A, r, c, e, sigma_allow):
    # פרמטרים לדוגמה
    #A, E, L, r, e, c = 5000, 200000, 3000, 50, 20, 100
    # נוסחת הסקנט #
    sec_term = 1 / np.cos(((L/(2*r)) * np.sqrt(P/(E*A))))
    sigma_max = (P/A) * (1 + (e*c/r**2) * sec_term)
    return sigma_max - sigma_allow

def find_critical_load(L, E, A, r, c, e, sigma_allow):
    P_critical = optimize.newton(lambda P: column_stress_error(P, L, E, A, r, c, e, sigma_allow), 500000)
    return P_critical

# בדיקה של הפונקציה עם הפרמטרים מההערה
if __name__ == "__main__":
    # הגדרת המשתנים לפי הערכים שרשומים אצלך בהערה:
    A = 5000
    E = 200000
    L = 3000
    r = 50
    e = 20
    c = 100
    sigma_allow = 100  # הערך המותר למאמץ
    
    try:
        p_crit = find_critical_load(L, E, A, r, c, e, sigma_allow)
        print(f"העומס הקריטי שנמצא (P_critical): {p_crit:.2f}")
    except Exception as e:
        print(f"אירעה שגיאה בחישוב: {e}")
