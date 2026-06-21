import numpy as np
from scipy import optimize

def column_stress_error(P, L, E, A, r, c, e, sigma_allow):
    # אם העומס הוא 0 או שלילי, המאמץ הוא 0 ולכן השגיאה היא מינוס המותר
    if P <= 0:
        return -sigma_allow
        
    # חישוב הביטוי שבתוך הקוסינוס
    cos_argument = (L / (2 * r)) * np.sqrt(P / (E * A))
    
    # הגנה מתמטית: אם הקוסינוס מתקרב לאפס או שלילי (עברנו את נקודת הקריסה התיאורטית)
    if cos_argument >= np.pi / 2:
        return float('inf') # מחזיר אינסוף כדי לסמן לרובוט לחזור אחורה
        
    sec_term = 1 / np.cos(cos_argument)
    sigma_max = (P / A) * (1 + (e * c / r**2) * sec_term)
    return sigma_max - sigma_allow

def find_critical_load(L, E, A, r, c, e, sigma_allow):
    # שימוש ב-brentq בטווח בטוח בין 0 לעומס עצום (למשל A * sigma_allow)
    # השיטה הזו חסינה לקריסות ומובטח שתמצא את התשובה
    P_critical = optimize.brentq(
        lambda P: column_stress_error(P, L, E, A, r, c, e, sigma_allow),
        0.0, 
        float(A * sigma_allow)
    )
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
