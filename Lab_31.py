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
    #

def day_of_year(year, month, day): # La función llamada day_of_year que toma tres parámetros
    
    days = 0 # Se inicializa una variable days en 0. Esta variable acumulará el total de días transcurridos desde el inicio del año hasta el mes anterior al mes dado.
    
    for m in range(1, month): # Se inicia un bucle for que itera sobre los meses desde 1 (enero) hasta month - 1 (el mes anterior al mes dado).
        
        md = days_in_month(year, m) # En cada iteración del bucle, se llama a la función days_in_month para obtener la cantidad de días en el mes m del año year
        
        if md == None: # Se verifica si la función days_in_month devolvió None. Esto podría suceder si la función no puede calcular la cantidad de días (por ejemplo, si el mes o el año no son válidos).
            
            return None # devuelve None
        days += md # Si md no es None, se suma la cantidad de días del mes actual (md) a la variable days.
        
    md = days_in_month(year, month) # Después del bucle, se llama a la función days_in_month para obtener la cantidad de días en el mes actual (month).
    
    if day >= 1 and day <= md: # Se verifica si el día dado (day) es válido para el mes actual. El día debe ser mayor o igual a 1 y menor o igual a la cantidad de días en el mes (md).
        
        return days + day # Si el día es válido, se devuelve el total acumulado de días (days) más el día actual (day). Esto representa el día del año (de 1 a 365 o 366).
    else: # Si el día no es válido (por ejemplo, day = 32 en un mes que solo tiene 31 días), se ejecuta este bloque.
        
        return None # devuelve None

print(day_of_year(2000, 12, 31)) # Se llama a la función day_of_year con la fecha 31 de diciembre de 2000. El resultado se imprime en la consola.
