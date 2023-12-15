numero = int(input("Introduce un número del 1 al 10: "))
def mostrar_tabla(numero):
    """Función que recibe un número entero del 1 al 10 y lee el fichero tabla-n.txt 
    con la tabla de multiplicar de ese número y lo muestra por pantalla
Parámetros:
- numero: La variable del número que se pregunta anteriormente al usuario
Salida:
Si el fichero existe lo muestra por pantalla y si no mostrará que no existe.
"""
    fil = "tabla-" + str(numero) + ".txt" 
    try:
        file = open(fil, "r")
        lineas = file.readlines()
        for a in lineas:
            x = a.replace("\n", "")
            print(x)
        file.close()
    except FileNotFoundError:
        print("El fichero no existe")
mostrar_tabla(numero)