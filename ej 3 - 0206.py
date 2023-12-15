n = int(input("Introduce un número del 1 al 10: "))
m = int(input("Introduce un segundo número del 1 al 10: "))
def mostrar_tabla(n, m):
    """Función que recibe dos números enteros del 1 al 10 y lee el fichero tabla-n.txt 
    con la tabla de multiplicar de n y muestra por pantalla la linea m del fichero
Parámetros:
- n: La variable del primer número que se pregunta anteriormente al usuario referente al fichero
- m: La variable del segundo número que se pregunta anteriormente al usuario referente a la línea del fichero
Salida:
Muestra por pantalla la línea m del fichero n, y si no existe lo mostrará, así como si no hay la línea m mostrará error.
"""
    if 1 <= n <= 10 and 1 <= m:
        fil = "tabla-" + str(n) + ".txt" 
        try:
            file = open(fil, "r")
            lineas = file.readlines()
            if 1 <= m <= len(lineas):
                linea_m = lineas[m - 1]
                print(linea_m)
            else:
                print("Error en m")
            file.close()
        except FileNotFoundError:
            print("El fichero no existe")
mostrar_tabla(n, m)