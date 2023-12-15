numero = int(input("Introduce un número del 1 al 10: "))
def tabla(numero):
    """Función que recibe un número entero del 1 al 10 y lo guarda en un fichero con el nombre 
    tabla-n.txt la tabla de multiplicar de ese número
Parámetros:
- numero: La variable del número que se pregunta anteriormente al usuario
Salida:
Crea el fichero con la tabla de multiplicar del número escogido.
"""
    fil = "tabla-" + str(numero) + ".txt" 
    file = open(fil, "w")
    for multiplicador in range(1, 11):
        file.write(str(numero) + "x" + str(multiplicador) + "=" + str(numero * multiplicador) + "\n")
    file.close()
tabla(numero)