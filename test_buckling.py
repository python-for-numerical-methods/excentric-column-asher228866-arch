import numpy as np
from scipy import optimize

def column_stress_error(P, L, E, A, r, c, e, sigma_allow):
    # חישוב האיבר שבתוך הקוסינוס (ברדיאנים)
    cos_argument = (L / (2 * r)) * np.sqrt(P / (E * A))
    
    # נוסחת הסקנט למציאת המאמץ המקסימלי
    sigma_max = (P / A) * (1 + (e * c / r**2) * (1 / np.cos(cos_argument)))
    
    # מחזירים את ההפרש - ניוטון-רפסון ישאף להביא אותו ל-0
    return sigma_max - sigma_allow

def find_critical_load(L, E, A, r, c, e, sigma_allow):
    # נקודת ניחוש ראשונית (למשל 100,000 ניוטון או כל ערך הגיוני אחר)
    initial_guess = 500000 
    
    # תיקון: שינוי ה-I ל-L כפי שהוגדר בפונקציה
    p_critical = optimize.newton(lambda P: column_stress_error(P, L, E, A, r, c, e, sigma_allow), initial_guess)     
    return p_critical
