def is_year_leap(year):
    if year % 4 != 0:
        return False  # No es divisible por 4, no es bisiesto
    elif year % 100 != 0:
        return True  # Es divisible por 4 pero no por 100, es bisiesto
    elif year % 400 == 0:
        return True  # Es divisible por 400, es bisiesto
    else:
        return False  # Es divisible por 100 pero no por 400, no es bisiesto
     
     
def days_in_month(year, month):
    
    # Lista con la cantidad de días en cada mes (para un año no bisiesto)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Si el mes es febrero (mes 2) y el año es bisiesto, devuelve 29 días
    if month == 2 and is_year_leap(year):
        return 29
    else:
        # Devuelve la cantidad de días correspondiente al mes
        return month_days[month - 1]

test_years = [1900, 2000, 2016, 1987, 2025]
test_months = [2, 2, 1, 11, 3]
test_results = [28, 29, 31, 30, 25]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
        
        
"""
EJEMPLO NONE:

def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(1))"""


"""
RETURN con una expresión

def boring_function():
    return 123
 
x = boring_function()
 
print("La función boring_function ha devuelto su resultado. Es:", x)
 
El fragmento de código escribe el siguiente texto en la consola:

La función boring_function ha devuelto su resultado. Es: 123"""