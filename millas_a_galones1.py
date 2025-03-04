"""4.3.8   LAB   Conversión del consumo de combustible
El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. Por ejemplo, en Europa, se muestra como la cantidad de combustible consumido por cada 100 kilómetros.

En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de combustible.

Tu tarea es escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa.

Las funciones:

se llaman liters_100km_to_miles_gallon y miles_gallon_to_liters_100km respectivamente;
toman un argumento (el valor correspondiente a sus nombres)
Complementa el código en el editor y ejecuta tu código y verifica si tu salida es la misma que la nuestra.

Aquí hay información para ayudarte:

1 milla = 1609.344 metros.
1 galón = 3.785411784 litros.

1. Convertir de L/100 km a mpg (millas por galón):
mpg = 235.2146 / L/100km


2. Convertir de mpg (millas por galón) a L/100 km:

L/100km = 235.2146 / mpg
"""

def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

    # Escribe tu código aquí.
    #

def miles_gallon_to_liters_100km(miles):
    liters = 235.2146 / miles
    return liters
    
    #
    # Escribe tu código aquí.
    #

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))